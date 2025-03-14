from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer
from django.views import View
from datetime import datetime
from django.http import JsonResponse
import json

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.filter(payment_status='success')  # Filter added here
    serializer_class = AppointmentSerializer

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.filter(payment_status='success')  # Filter added here
    serializer_class = AppointmentSerializer

class DoctorAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return Appointment.objects.filter(doctor_id=doctor_id, payment_status='success')  # Filter added here

class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Appointment.objects.filter(patient_id=patient_id, payment_status='success')  # Filter added here


class AvailableAppointmentTimesView(View):
    def get(self, request, doctor_id,appointment_date):
        appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
        # Assuming doctor_id is the ID of the doctor for whom you want to get available times
        doctor_appointments = Appointment.objects.filter(doctor_id=doctor_id, appointment_date=appointment_date)
        booked_times = set(appointment.appointment_time for appointment in doctor_appointments)

        # List of all available times
        all_times = ['09:00', '09:20', '09:40', '10:00', '10:20', '10:40', '11:00', '11:20', '11:40',
                     '12:00', '12:20', '12:40', '13:00', '13:20', '13:40', '14:00']

        # Filter out booked times to get available times
        available_times = [time for time in all_times if time not in booked_times]

        return JsonResponse({'times': available_times})


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class UpdatePaymentStatusView(View):
    def post(self, request, appointment_id):
        try:
            appointment = Appointment.objects.get(pk=appointment_id)
        except Appointment.DoesNotExist:
            return JsonResponse({"error": "Appointment not found"}, status=404)

        # Assuming you receive the new payment_status value in the request data
        json_data = json.loads(request.body.decode('utf-8'))
        new_payment_status = json_data.get('payment_status')
        # Update the payment_status field
        appointment.payment_status = new_payment_status
        appointment.save()

        # Serialize the updated appointment data
        serializer = AppointmentSerializer(appointment)

        return JsonResponse(serializer.data, status=200)