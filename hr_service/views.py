# auth_service/views.py
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Employee
from django.contrib import messages
# from .forms import EmployeeForm

def logout_view(request):
    return HttpResponse("logout view for auth_service")

def employee_list(request):
    employees = Employee.objects.all()  
    print(employees)
    return render(request, 'hr_service/employee_list.html', {'employees': employees})

def calendar(request):
     return render(request, 'hr_service/calendar.html')

def timeline(request):
     return render(request, 'hr_service/timeline.html')

def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)  

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('employee_list')  
    else:
        form = EmployeeForm(instance=employee)  

    return render(request, 'employee_edit.html', {'form': form, 'employee': employee})

