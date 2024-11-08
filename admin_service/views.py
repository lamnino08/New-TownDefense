# auth_service/views.py
import json
from django.http import JsonResponse
from django.shortcuts import render
from grpc import Status
from requests import Response
from .service import get_staff_data, get_roles_data, get_departments_data, get_filtered_staff, create_staff_account, update_staff, get_a_staff_data, update_staff_status, delete_a_staff
from django.views.decorators.csrf import csrf_exempt

def get_view_dashboard(request):
    panel = request.GET.get('panel', 'account')
        
    if panel == 'account':
        staff_data = get_staff_data()
        roles = get_roles_data()
        departments = get_departments_data()
        context = {
            'panel': 'account',
            'employees': staff_data,
            'departments': departments,
            'roles': roles
        }
    elif panel == 'main':
        date = request.GET.get('date')
        context = {
            'panel': 'main',
        }
    elif panel == 'structure':
        print('here')
        context = {'panel': 'structure'}

    return render(request, 'admin_service/index.html', context)

def filter_staff(request):
    name = request.GET.get('name', None)
    department = request.GET.get('department', None)
    role = request.GET.get('role', None)
    
    employee = get_filtered_staff(name=name, department=department, role=role)
    return JsonResponse(employee, safe=False)

@csrf_exempt
def create_staff_api(request):
    if request.method == 'POST':
        # Extract data from the request and pass it to your service layer
        data = json.loads(request.body)
        result = create_staff_account(data)

        if result['status'] == 'success':
            return JsonResponse({'message': 'Account created successfully!'}, status=201)
        else:
            return JsonResponse({'error': result['message']}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def edit_staff_api(request, staff_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            updated_staff = update_staff(staff_id, data)
            print(update_staff)
            return JsonResponse({
                "success": True,
                "message": "Employee details updated successfully.",
                "data": updated_staff
            }, status=200)
        
        except Exception as e:
            print(e)
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        
def get_staff_api(request, staff_id):
    if request.method == 'GET':
        result = get_a_staff_data(staff_id)

        if result['status'] == 'success':
            print(result)
            return JsonResponse({'status': 'success', 'data': result['data']}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': result['message']}, status=404)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def update_status_staff(request, staff_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_status = data.get('status')

            result = update_staff_status(staff_id, new_status)

            print(result)
            if result['status'] == 'success':
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'error': result['message']}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_staff(request, staff_id):
    if request.method == 'DELETE':
        result = delete_a_staff(staff_id)
        if result['status'] == 'success':
            return JsonResponse(result, status=200)
        return JsonResponse(result, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


