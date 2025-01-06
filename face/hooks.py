app_name = "face"
app_title = "Face"
app_publisher = "mostafa"
app_description = "test"
app_email = "mostafa@gmail.com"
app_license = "mit"
page_js = {
    "face": "public/js/face_recognition.js"
}
fixtures = [
    {
        "doctype": "DocType",  # Correct case-sensitive name
        "filters": [
            ["module", "=", "Face"]  # Ensure this matches the module name of your app
        ]
    },
    {
        "doctype": "Property Setter"
    },
    {
        "doctype": "Custom Field"
    }
]
after_install = "face.utils.install_dependencies"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "face",
# 		"logo": "/assets/face/logo.png",
# 		"title": "Face",
# 		"route": "/face",
# 		"has_permission": "face.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/face/css/face.css"
# app_include_js = "/assets/face/js/face.js"

# include js, css files in header of web template
# web_include_css = "/assets/face/css/face.css"
# web_include_js = "/assets/face/js/face.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "face/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "face/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "face.utils.jinja_methods",
# 	"filters": "face.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "face.install.before_install"
# after_install = "face.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "face.uninstall.before_uninstall"
# after_uninstall = "face.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "face.utils.before_app_install"
# after_app_install = "face.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "face.utils.before_app_uninstall"
# after_app_uninstall = "face.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "face.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"face.tasks.all"
# 	],
# 	"daily": [
# 		"face.tasks.daily"
# 	],
# 	"hourly": [
# 		"face.tasks.hourly"
# 	],
# 	"weekly": [
# 		"face.tasks.weekly"
# 	],
# 	"monthly": [
# 		"face.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "face.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "face.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "face.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["face.utils.before_request"]
# after_request = ["face.utils.after_request"]

# Job Events
# ----------
# before_job = ["face.utils.before_job"]
# after_job = ["face.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"face.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

