from rest_framework import serializers, viewsets
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_doctor', 'is_patient', 'firstname', 'lastname', 'phone', 'age', 'address', 'city', 'country', 'postcode', 'dob', 'gender']

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
