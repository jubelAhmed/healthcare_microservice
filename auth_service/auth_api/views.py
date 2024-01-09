# healthcare_app/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()
        user_type = "patient"
        if user.is_doctor:
            user_type = "doctor"
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'user_type': user_type,
            }
            return Response(response_data)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
        
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
        
        
class DoctorListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        doctors = CustomUser.objects.filter(is_doctor=True)
        serializer = UserSerializer(doctors, many=True)
        return Response(serializer.data)

class PatientListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        patients = CustomUser.objects.filter(is_patient=True)
        serializer = UserSerializer(patients, many=True)
        return Response(serializer.data)
    

class DoctorDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.filter(is_doctor=True)
    serializer_class = UserSerializer

class PatientDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.filter(is_patient=True)
    serializer_class = UserSerializer