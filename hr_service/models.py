from django.db import models

class Employee(models.Model):

    StaffID  = models.PositiveIntegerField(primary_key=True)  
    

    Name  = models.TextField(null=True, blank=True)  
    

    PhoneNumber  = models.TextField()  
    

    RoleID  = models.PositiveIntegerField(null=True, blank=True)  
    
    
    Password = models.TextField(null=True, blank=True)  
    
    
    Status  = models.BooleanField(default=True)  
    
    
    CreateAt  = models.DateTimeField(null=True, blank=True)  
    
    
    username = models.TextField(null=True, blank=True)  

    class Meta:
        db_table = 'staff' 

    def __str__(self):
        return self.Name or "Unnamed Employee"
    
class Salary(models.Model):
    staff_id = models.PositiveIntegerField()  
    amount = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'salary'  

    def __str__(self):
        return f"Salary for StaffID {self.staff_id}: {self.amount}"
    
class ShiftOfStaff(models.Model):
    shift_of_staff_id = models.AutoField(primary_key=True)  
    shift_id = models.PositiveIntegerField(null=True, blank=True)  
    staff_id = models.PositiveIntegerField(null=True, blank=True)  
    is_confirm = models.BooleanField(null=True, blank=True)  
    is_attendant = models.BooleanField(null=True, blank=True)  

    class Meta:
        db_table = 'shiftofstaff'  

    def __str__(self):
        return f"ShiftOfStaff {self.shift_of_staff_id} for StaffID {self.staff_id}"

class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True)  
    time_start = models.DateTimeField(null=True, blank=True) 
    time_end = models.DateTimeField(null=True, blank=True)  
    class Meta:
        db_table = 'shift' 

    def __str__(self):
        return f"Shift {self.shift_id}: {self.time_start} - {self.time_end}"


