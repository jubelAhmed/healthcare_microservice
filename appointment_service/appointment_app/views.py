from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DoctorAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return Appointment.objects.filter(doctor_id=doctor_id).values('appointment_id', 'doctor_id', 'patient_id', 'appointment_time', 'purpose', 'sick_information', 'created_at', 'updated_at')

class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Appointment.objects.filter(patient_id=patient_id).values('appointment_id', 'doctor_id', 'patient_id', 'appointment_time', 'purpose', 'sick_information', 'created_at', 'updated_at')
