frappe.pages['face'].on_page_load = function (wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Face Recognition',
        single_column: true
    });

    // Add a placeholder for buttons and camera
    $(page.body).html(`
        <div id="button-section" style="text-align: center; margin-top: 100px;">
            <button id="register-face-btn" class="btn btn-primary" style="margin: 20px; width: 200px; height: 50px; font-size: 16px;">Register Face</button>
            <button id="check-in-out-btn" class="btn btn-secondary" style="margin: 20px; width: 200px; height: 50px; font-size: 16px;">Check In/Out</button>
        </div>
        <div id="camera-section" style="text-align: center; margin-top: 50px; display: none;">
            <video id="camera-stream" autoplay playsinline style="width: 100%; max-width: 640px;"></video>
            <canvas id="capture-canvas" style="display: none;"></canvas>
            <br>
            <button id="stop-camera-btn" class="btn btn-danger" style="margin-top: 20px; display: none;">Stop Camera</button>
        </div>
    `);

    // Register Face button logic
    $('#register-face-btn').click(function () {
        frappe.prompt(
            [
                {
                    fieldname: 'employee_full_name',
                    label: 'Full Name',
                    fieldtype: 'Data',
                    reqd: 1,
                    description: "Enter the full name of the employee to register their face."
                }
            ],
            (values) => {
                startCamera();

                // Add capture button for Register Face
                $('#camera-section').append(`
                    <button id="capture-register-btn" class="btn btn-primary" style="margin-top: 20px;">Capture</button>
                `);

                // Capture image logic
                $('#capture-register-btn').click(function () {
                    captureImage((imageData) => {
                        // Call the backend to register the face
                        frappe.call({
                            method: 'face.api.register_face',
                            args: {
                                employee_full_name: values.employee_full_name,
                                image_data: imageData
                            },
                            callback: (response) => {
                                frappe.msgprint(response.message || 'Face registered successfully.');
                                stopCamera();
                            }
                        });
                    });
                });
            },
            'Register Face',
            'Submit'
        );
    });

    // Check In/Out button logic
    $('#check-in-out-btn').click(function () {
        startCamera();

        // Automatically capture the image after a delay
        setTimeout(() => {
            captureImage((imageData) => {
                // Call the backend to check in/out
                frappe.call({
                    method: 'face.api.clock_in_out',
                    args: {
                        image_data: imageData
                    },
                    callback: (response) => {
                        frappe.msgprint(response.message || 'Action completed successfully.');
                        stopCamera();
                    }
                });
            });
        }, 3000); // 3-second delay
    });

    // Helper function to start the camera
    function startCamera() {
        $('#camera-section').show();
        navigator.mediaDevices
            .getUserMedia({ video: true })
            .then((stream) => {
                const video = document.getElementById('camera-stream');
                video.srcObject = stream;

                // Show stop button
                $('#stop-camera-btn').show().click(() => stopCamera());
            })
            .catch((err) => {
                frappe.msgprint(`Error accessing camera: ${err.message}`);
            });
    }

    // Helper function to stop the camera
    function stopCamera() {
        const video = document.getElementById('camera-stream');
        const stream = video.srcObject;
        if (stream) {
            stream.getTracks().forEach((track) => track.stop());
            video.srcObject = null;
        }
        $('#camera-section').hide();
        $('#stop-camera-btn').hide();
        $('#capture-register-btn').remove(); // Remove capture button for Register Face
    }

    // Helper function to capture an image
    function captureImage(callback) {
        const video = document.getElementById('camera-stream');
        const canvas = document.getElementById('capture-canvas');
        const context = canvas.getContext('2d');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        const imageData = canvas.toDataURL('image/png');
        callback(imageData);
    }
};

