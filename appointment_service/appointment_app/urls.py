from django.urls import path
from .views import AppointmentListCreateView, AppointmentDetailView,  PatientAppointmentListView
from .views import DoctorAppointmentListView, AvailableAppointmentTimesView
urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('doctors/<int:doctor_id>/appointments/', DoctorAppointmentListView.as_view(), name='doctor-appointment-list'),
    path('patients/<int:patient_id>/appointments/', PatientAppointmentListView.as_view(), name='patient-appointment-list'),
    path('appointment-times/<int:doctor_id>/<str:appointment_date>/', AvailableAppointmentTimesView.as_view(), name='doctor_available_time'),
]
