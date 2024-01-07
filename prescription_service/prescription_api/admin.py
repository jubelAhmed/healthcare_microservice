from django.contrib import admin

from prescription_api.models import Prescription, MedicalTest, Medication, PatientCondition
# Register your models here.

admin.site.register(Prescription)
admin.site.register(MedicalTest)
admin.site.register(Medication)
admin.site.register(PatientCondition)