from frappe.model.document import Document
import frappe


class CRMRegistration(Document):
    def before_save(self):
        user = frappe.db.exists("User", self.email)
        if not user:
            new_user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "username": self.first_name.lower()
                # Add other fields here as necessary
            })
            new_user.insert(ignore_permissions=True)

