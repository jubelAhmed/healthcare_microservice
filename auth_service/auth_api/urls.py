# healthcare_app/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/users/', views.UserListCreateView.as_view(), name='api-user-list-create'),
    path('api/users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='api-user-retrieve-update-destroy'),

    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),

    path('patients/', views.PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),


]
