import frappe
import os
import base64
import json
import face_recognition
from datetime import datetime, time

# Directory to store face images
FACE_IMAGES_DIR = frappe.get_site_path("public", "files", "face_images")
os.makedirs(FACE_IMAGES_DIR, exist_ok=True)

@frappe.whitelist()
def register_face(employee_full_name, image_data):
    """
    Register a face for an employee from captured image data.
    """
    if not employee_full_name:
        return {"status": "error", "message": "Employee full name is required."}

    # Decode the base64 image data
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)

    # Save the image
    img_name = f"{employee_full_name.replace(' ', '_')}.png"
    img_path = os.path.join(FACE_IMAGES_DIR, img_name)
    with open(img_path, "wb") as img_file:
        img_file.write(image_bytes)

    # Save the face encoding
    image = face_recognition.load_image_file(img_path)
    face_encodings = face_recognition.face_encodings(image)
    if not face_encodings:
        return {"status": "error", "message": "No face detected in the image."}

    face_encoding = face_encodings[0].tolist()

    # Save to the database
    doc = frappe.get_doc({
        "doctype": "Employee-face",
        "full_name": employee_full_name,
        "face_encoding": json.dumps(face_encoding),  # Serialize as JSON
        "image_path": img_path
    })
    doc.insert()
    frappe.db.commit()

    return {"status": "success", "message": f"Face registered for {employee_full_name}"}


@frappe.whitelist()
def clock_in_out(image_data):
    """
    Recognize a face and record clock in/out.
    """
    # Define allowed check-in and check-out times
    clock_in_start = time(9, 0)  # 9:00 AM
    clock_in_end = time(10, 0)  # 10:00 AM
    clock_out_start = time(17, 0)  # 5:00 PM

    # Decode the base64 image data
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)

    # Save the temporary image
    temp_img_path = os.path.join(FACE_IMAGES_DIR, "temp_image.png")
    with open(temp_img_path, "wb") as img_file:
        img_file.write(image_bytes)

    # Load the image and encode
    image = face_recognition.load_image_file(temp_img_path)
    face_encodings = face_recognition.face_encodings(image)
    if not face_encodings:
        return {"status": "error", "message": "No face detected in the image."}

    face_encoding = face_encodings[0]

    # Compare with existing employees
    employees = frappe.get_all("Employee-face", fields=["name", "full_name", "face_encoding"])
    for employee in employees:
        known_encoding = json.loads(employee.face_encoding)  # Deserialize the JSON string
        match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
        if match:
            now = datetime.now()
            current_time = now.time()
            date = frappe.utils.nowdate()

            # Check existing attendance for the day
            existing_attendance = frappe.get_all(
                "Attendance-face",
                filters={"full_name": employee.full_name, "date": date},
                fields=["name", "clock_in_time", "clock_out_time"]
            )

            # Handle check-in logic
            if clock_in_start <= current_time < clock_in_end:
                if existing_attendance:
                    return {"status": "error", "message": f"{employee.full_name} has already checked in."}

                # Record new clock-in time
                doc = frappe.get_doc({
                    "doctype": "Attendance-face",
                    "full_name": employee.full_name,
                    "date": date,
                    "clock_in_time": frappe.utils.nowtime()
                })
                doc.insert()
                frappe.db.commit()
                return {"status": "success", "message": f"{employee.full_name} checked in successfully."}

            # Handle check-out logic
            elif current_time >= clock_out_start:
                if existing_attendance and existing_attendance[0].get("clock_out_time"):
                    return {"status": "error", "message": f"{employee.full_name} has already checked out."}

                # Update clock-out time
                if existing_attendance:
                    attendance = frappe.get_doc("Attendance-face", existing_attendance[0]["name"])
                    attendance.clock_out_time = frappe.utils.nowtime()
                    attendance.save()
                    frappe.db.commit()
                    return {"status": "success", "message": f"{employee.full_name} checked out successfully."}

            # Invalid action during working hours
            return {"status": "error", "message": "Invalid action: Working hours are between 10:00 AM and 5:00 PM."}

    return {"status": "error", "message": "No matching face found."}

