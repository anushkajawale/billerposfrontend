from django.db import models
class Employees(models.Model):
  


    # Basic Information
    Employees_id = models.AutoField(primary_key=True)
    Employees_firstname = models.CharField(max_length=100)
    Employees_middlename = models.CharField(max_length=100, blank=True, null=True)
    Employees_lastname = models.CharField(max_length=100)
    Employees_dateof_birth = models.DateField(null=True, blank=True)
    Employees_gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    # Contact Information
    Employees_address = models.TextField()
    Employees_mobile_number = models.CharField(max_length=15)
    Employees_email = models.EmailField(unique=True)

    # Education & Qualifications
    Employees_highesteducation = models.CharField(max_length=200)
    Employees_institutionsattended = models.CharField(max_length=200)
    Employees_degreesearned = models.CharField(max_length=200)
    Employees_certifications = models.CharField(max_length=200, blank=True, null=True)

    # Leave & Time Off
    Employees_vacationleave_balance = models.IntegerField(default=0)
    Employees_sickleave_balance = models.IntegerField(default=0)
    Employees_leavetypes = models.TextField(blank=True, null=True)

    # Compensation Details
    Employees_salary = models.DecimalField(max_digits=10, decimal_places=2)
    Employees_payfrequency = models.CharField(max_length=50, choices=[('Monthly', 'Monthly'), ('Bi-Weekly', 'Bi-Weekly'), ('Weekly', 'Weekly')])
    Employees_accountnumber = models.CharField(max_length=30)
    Employees_ifsccode = models.CharField(max_length=15)
    Employees_accountholder_name = models.CharField(max_length=100)

    # Employment Details
    employee_id = models.CharField(max_length=50, unique=True)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Terminated', 'Terminated')])
    hire_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(blank=True, null=True)

    # Emergency Contact
    Employees_emergencycontact_name = models.CharField(max_length=100)
    Employees_emergencycontact_relationship = models.CharField(max_length=50)
    Employees_emergencycontact_phone = models.CharField(max_length=15)

    # Work History
    Employees_previous_employers = models.TextField(blank=True, null=True)
    Employees_previous_jobtitles = models.TextField(blank=True, null=True)
    Employees_previous_responsibilities = models.TextField(blank=True, null=True)
    department_name = models.CharField(max_length=100)
    department_birth = models.DateField(null=True, blank=True)

    # Documents & Attachments
    Employees_resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    Employees_iddocument = models.FileField(upload_to='id_documents/', blank=True, null=True)
    Employees_certificationsdocument = models.FileField(upload_to='certifications/', blank=True, null=True)
    d_relationship = models.CharField(max_length=100, null=True, blank=True)

    
    
    class Meta:
        db_table = "tbl_Employees"
    
    def __str__(self):
        return self.Employees_firstname

# Create your models here.
