# auth_service/views.py
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .service import login_user 

def login_view(request):
    if 'username' in request.session:
        # Redirect to the dashboard if the session exists
        return redirect('/dashboard/') 
    return render(request, 'auth_service/login.html')

@csrf_exempt  
def login_api(request):
        try:    
            # Parse JSON data
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            result = login_user(username, password)
            status_code = 200 if result["status"] == "success" else 401
            
            if result["status"] == "success":
                # Extract staff and role information
                staff = result["staff"]
                role = staff["role"]
                
                # Store necessary session data
                request.session['username'] = staff["username"]
                request.session['staff_id'] = staff["staff_id"]
                request.session['role_id'] = role["role_id"]
                request.session['firstPage'] = role["firstPage"]

                # Return the success response with the firstPage for redirection
                return JsonResponse({
                    "status": "success",
                    "message": "Login successful",
                    "firstPage": role["firstPage"],
                }, status=200)
            else:
                # Return error message if authentication failed
                return JsonResponse(result, status=401)
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)

def logout_view(request):
    # Here you can add logic for login, for now, we’ll return a simple message
    return HttpResponse("logout view for auth_service")
