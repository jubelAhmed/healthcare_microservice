from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'doctor_id', 'patient_id', 'appointment_time', 'purpose', 'created_at', 'updated_at')
    list_filter = ('doctor_id', 'patient_id', 'appointment_time')  # Add filters if needed

admin.site.register(Appointment, AppointmentAdmin)