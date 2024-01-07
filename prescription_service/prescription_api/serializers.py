from rest_framework import serializers
from .models import Prescription, Medication, MedicalTest, PatientCondition

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
        extra_kwargs = {
            'prescription': {'required': False}
        }

class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = '__all__'
        extra_kwargs = {
            'prescription': {'required': False}
        }

class PatientConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCondition
        fields = '__all__'
        extra_kwargs = {
            'prescription': {'required': False}
        }

class PrescriptionSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True, required=False)
    medical_tests = MedicalTestSerializer(many=True, required=False)
    medication_conditions = PatientConditionSerializer(many=True, required=False)

    class Meta:
        model = Prescription
        fields = '__all__'

    def create(self, validated_data):
        medications_data = validated_data.pop('medications', [])
        medical_tests_data = validated_data.pop('medical_tests', [])
        medication_conditions_data = validated_data.pop('medication_conditions', [])

        prescription = Prescription.objects.create(**validated_data)

        for medication_data in medications_data:
            Medication.objects.create(prescription=prescription, **medication_data)

        for medical_test_data in medical_tests_data:
            MedicalTest.objects.create(prescription=prescription, **medical_test_data)

        for medication_condition_data in medication_conditions_data:
            PatientCondition.objects.create(prescription=prescription, **medication_condition_data)

        return prescription
    
    def update(self, instance, validated_data):
        medications_data = validated_data.get('medications', [])
        for medication_data in medications_data:
            medication, created = Medication.objects.update_or_create(
                prescription=instance,
                medicine_name=medication_data.get('medicine_name'),
                defaults={
                    'doses': medication_data.get('doses', ''),
                    'route': medication_data.get('route', ''),
                    'frequency': medication_data.get('frequency', ''),
                    # Add other fields as needed
                }
            )

        # Update medical tests
        medical_tests_data = validated_data.get('medical_tests', [])
        for medical_test_data in medical_tests_data:
            medical_test, created = MedicalTest.objects.update_or_create(
                prescription=instance,
                test_name=medical_test_data.get('test_name'),
                defaults={
                    'description': medical_test_data.get('description', ''),
                    # Add other fields as needed
                }
            )

        # Update medication conditions
        medication_conditions_data = validated_data.get('medication_conditions', [])
        for medication_condition_data in medication_conditions_data:
            condition, created = PatientCondition.objects.update_or_create(
                prescription=instance,
                condition_name=medication_condition_data.get('condition_name'),
                defaults={
                    'description': medication_condition_data.get('description', ''),
                    # Add other fields as needed
                }
            )

        instance.save()
        return instance


