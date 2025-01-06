from frappe import _

def get_data():
    return [
        {
            "module_name": "Face",
            "label": _("Face"),
            "type": "page",
            "link": "face",  
            "icon": "octicon octicon-device-camera",  
            "color": "#3498db",  
        }
    ]

