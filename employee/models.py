from django.db import models

# Create your models here.
class Employee(models.Model):
    """
    EmployeeId
    first_name
    last_name
    title
    """
    TITLE_CHOICE = [
        ('MR.', 'Mr.'),
        ('MISS.', 'Miss.'),
        ('MS.', 'Ms.'),
        ('MRS.', 'Mrs.'),
        ('DR.', 'Dr.'),
    ]
    employeeID = models.BigAutoField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=5, choices=TITLE_CHOICE, default='Dr.')
