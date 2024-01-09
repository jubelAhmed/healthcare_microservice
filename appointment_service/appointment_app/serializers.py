from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    appointment_time = serializers.ChoiceField(choices=Appointment.appointment_time.field.choices)

    class Meta:
        model = Appointment
        fields = '__all__'
