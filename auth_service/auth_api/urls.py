# healthcare_app/urls.py
from django.urls import path
from .views import RegisterView, LoginView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/users/', UserListCreateView.as_view(), name='api-user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='api-user-retrieve-update-destroy'),
]
