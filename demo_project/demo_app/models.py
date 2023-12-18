from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    CODE_PURPOSE_CHOICES = [
        ('enquiry', 'Enquiry'),
        ('placeorder', 'Place Order'),
        ('return', 'Return'),
    ]
    name = models.CharField(max_length=124)
    date_of_birth = models.DateField(default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    phone = models.IntegerField(default=None)
    mail = models.EmailField(null=True)
    address = models.CharField(max_length=250, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    materials = models.CharField(max_length=255, blank=True)


    purpose = models.CharField(max_length=20, choices=CODE_PURPOSE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name