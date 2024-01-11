from django.urls import path

from . import views

from django.views.generic.base import TemplateView 

urlpatterns = [
    path('confirm/<int:appointment_id>/<int:patient_id>/', views.transaction.as_view(), name='transaction'),
]