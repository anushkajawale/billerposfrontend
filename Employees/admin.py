from django.contrib import admin
from .models import Employees

class EmployeesAdmin(admin.ModelAdmin):
    list_display = [
        'Employees_firstname', 'Employees_middlename', 'Employees_lastname', 'Employees_dateof_birth', 'Employees_gender',
        'Employees_address', 'Employees_mobile_number', 'Employees_email',
        
        
        'Employees_highesteducation', 'Employees_institutionsattended', 'Employees_degreesearned', 'Employees_certifications',

       
        'Employees_vacationleave_balance', 'Employees_sickleave_balance', 'Employees_leavetypes',

       
        'Employees_salary', 'Employees_payfrequency', 'Employees_accountnumber', 'Employees_ifsccode', 'Employees_accountholder_name',

       
        'employee_id', 'job_title', 'department', 'employment_status',
        'hire_date', 'termination_date',

  
        'Employees_emergencycontact_name', 'Employees_emergencycontact_relationship', 'Employees_emergencycontact_phone',

        
        'Employees_previous_employers', 'Employees_previous_jobtitles', 'Employees_previous_responsibilities',

        'Employees_resume', 'Employees_iddocument', 'Employees_certificationsdocument'
    

    ]

admin.site.register(Employees, EmployeesAdmin)
