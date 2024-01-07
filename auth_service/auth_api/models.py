# healthcare_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
    )
    phone = models.CharField(max_length = 16, unique = True, null=True, blank=True)
    age = models.CharField(max_length=3,null=True)
    dob=models.DateField(null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64, null=True)
    Country = models.CharField(max_length=64, null=True)
    postcode = models.CharField(max_length=8, null=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    doctor_specialist = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.username
    class Meta:
        permissions = []

# Add related_name to groups field
CustomUser.groups.field.remote_field.related_name = 'customuser_groups'

# Add related_name to user_permissions field
CustomUser.user_permissions.field.remote_field.related_name = 'customuser_user_permissions'