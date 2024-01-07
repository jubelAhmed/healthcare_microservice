from django.urls import path
from .views import PrescriptionAPIView

urlpatterns = [
    path('prescriptions/', PrescriptionAPIView.as_view(), name='prescription-list'),
    path('prescriptions/<int:pk>/', PrescriptionAPIView.as_view(), name='prescription-detail'),
]
