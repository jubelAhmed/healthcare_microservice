from django.urls import path
from .views import AppointmentListCreateView, AppointmentDetailView,  PatientAppointmentListView
from .views import DoctorAppointmentListView, AvailableAppointmentTimesView, UpdatePaymentStatusView
urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('doctors/<int:doctor_id>/appointments/', DoctorAppointmentListView.as_view(), name='doctor-appointment-list'),
    path('patients/<int:patient_id>/appointments/', PatientAppointmentListView.as_view(), name='patient-appointment-list'),
    path('appointment-times/<int:doctor_id>/<str:appointment_date>/', AvailableAppointmentTimesView.as_view(), name='doctor_available_time'),
    path('update_payment_status/<int:appointment_id>/', UpdatePaymentStatusView.as_view(), name='update_payment_status'),

]
