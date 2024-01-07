from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    appointment_time = serializers.ChoiceField(choices=Appointment.appointment_time.field.choices)

    class Meta:
        model = Appointment
        fields = ['appointment_id', 'doctor_id', 'patient_id', 'appointment_time', 'appointment_date', 'purpose', 'sick_information', 'created_at', 'updated_at']
