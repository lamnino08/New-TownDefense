# auth_service/service.py
from .backends import StaffBackend  # Import your custom backend

def login_user(username, password):
    """
    Attempt to authenticate a user with the provided username and password.
    """
    staff_backend = StaffBackend()
    staff = staff_backend.authenticate(username=username, password=password)  

    if staff is not None:
        # Return a dictionary with success status and relevant staff details
        return {
            "status": "success",
            "staff": {
                "staff_id": staff.staff_id,
                "username": staff.username,
                "name": staff.name,
                "phone_number": staff.phone_number,
                # Add other necessary fields
            }
        }
        # Invalid credentials
        return {"status": "error", "message": "Invalid username or password"}
