from django.db import models

# Create your models here.
class Employee(models.Model):
    """ Create the Employee SQLite table.

    Primary key: Employee_id, used as Foreign key to appointments.

    Fields: first_name(String), last_name(String), title(Choice_field), phone(Integer),
            email(String)

    __str__: returns title and last name

    TODO: Add function to determine if the Employee is available for requested appointment.
    """
    # An array of professional titles for employees.
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
    phone = models.IntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.title, self.last_name)
