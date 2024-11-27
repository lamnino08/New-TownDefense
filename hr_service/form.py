from django import forms
from .models import CustomUser
from .models import WorkHistory
from .models import Shift
from .models import Attendance
from .models import Salary


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender', 'address', 'password']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['start_time', 'end_time', 'shift_type', 'salary_rate', 'notes', 'max_employees']

class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkHistory
        fields = ['employee', 'start_date', 'end_date', 'kpi', 'contract_type', 'contract_duration']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['shift', 'check_in', 'check_out']

class ShiftRegistrationForm(forms.Form):
    shift_id = forms.IntegerField(widget=forms.HiddenInput)

    def clean_shift_id(self):
        shift_id = self.cleaned_data['shift_id']
        try:
            shift = Shift.objects.get(id=shift_id)
        except Shift.DoesNotExist:
            raise forms.ValidationError("Ca làm việc không tồn tại.")
        return shift_id

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['base_salary']