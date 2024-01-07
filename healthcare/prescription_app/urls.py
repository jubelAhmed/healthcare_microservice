from django.urls import path
from . import views

urlpatterns = [
   path('', views.prescription, name='prescription'),
    path('update_prescription/<int:pk>/', views.update_prescription, name='update_prescription'),

]