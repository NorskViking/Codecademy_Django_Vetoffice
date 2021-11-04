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
    title = models.CharField(max_length=5, choices=TITLE_CHOICE, default='Dr.')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    #available = boolean
