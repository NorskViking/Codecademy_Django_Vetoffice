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
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=5, choices=TITLE_CHOICE, default='Dr.')
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    #available = boolean

    def __str__(self):
        return "%s %s" % (self.title, self.last_name)
