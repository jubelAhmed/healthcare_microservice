# healthcare_app/serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name','last_name','phone', 'age','address','city', 'Country', 'postcode', 'dob', 'gender', 'is_doctor', 'is_patient', 'doctor_specialist', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
