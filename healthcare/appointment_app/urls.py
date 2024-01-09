# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.appointment, name='appointment_create'),
    path('appointment_list/<int:user_id>/<str:user_type>/', views.appointment_list, name='appointment_list'),
    # # path('submit_appointment/', views.appointment_form, name='submit_appointment'),
    # path('doctorview/', views.doctor_view, name='doctor_view'),
    # path('patientview/', views.patient_view, name='patient_view'),
    # path('my-view/', views.my_view, name='my_view'),
    path('doctor_available_time/<int:doctor_id>/<str:appointment_date>/', views.available_time, name='doctor_available_time'),
]
