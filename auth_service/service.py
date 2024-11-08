# auth_service/service.py
from .backends import StaffBackend  # Import your custom backend

def login_user(username, password):
    """
    Attempt to authenticate a user with the provided username and password.
    """
    staff_backend = StaffBackend()
    staff = staff_backend.authenticate(username=username, password=password)

    if staff is not None:
        # Return a dictionary with success status, staff details, and role information
        return {
            "status": "success",
            "staff": {
                "staff_id": staff.staff_id,
                "username": staff.username,
                "name": staff.name,
                "phone_number": staff.phone_number,
                "role": {
                    "role_id": staff.role.role_id,
                    "description": staff.role.description,
                    "firstPage": staff.role.first_page,
                }
            }
        }
    else:
        # Invalid credentials
        return {"status": "error", "message": "Invalid username or password"}
