from django.urls import path
from . import views

urlpatterns = [
   path('view/<str:user_type>/<int:user_id>/', views.prescription, name='prescription'),
   path('create_prescription/<int:appointment_id>/<int:patient_id>/<int:doctor_id>/', views.create_prescription, name='create_prescription'),
   path('update_prescription/<int:pk>/', views.update_prescription, name='update_prescription'),
   path('details_prescription/<int:pk>/', views.details_prescription, name='details_prescription'),
]