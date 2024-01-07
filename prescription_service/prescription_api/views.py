from rest_framework import generics
from rest_framework.response import Response
from .models import Prescription, Medication, MedicalTest, PatientCondition
from .serializers import PrescriptionSerializer
from django.db.models import Prefetch

class PrescriptionAPIView(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        appointment_id = self.request.query_params.get('appointment_id', None)
        doctor_id = self.request.query_params.get('doctor_id', None)
        patient_id = self.request.query_params.get('patient_id', None)
        prescription_id = self.request.query_params.get('id', None)

        filters = {}

        if doctor_id:
            filters['doctor_id'] = doctor_id

        if patient_id:
            filters['patient_id'] = patient_id

        if appointment_id:
            filters['appointment_id'] = appointment_id
        
        if prescription_id:
            filters['id'] = prescription_id
            
 # Define prefetch related objects
        prefetch_related_objects = Prefetch(
            'medication_set',  # Replace with your related name or manager if you specified one in Medication model
            queryset=Medication.objects.all(),
            to_attr='medications'
        ), Prefetch(
            'medicaltest_set',  # Replace with your related name or manager if you specified one in MedicalTest model
            queryset=MedicalTest.objects.all(),
            to_attr='medical_tests'
        ), Prefetch(
            'patientcondition_set',  # Replace with your related name or manager if you specified one in PatientCondition model
            queryset=PatientCondition.objects.all(),
            to_attr='medication_conditions'
        )

        # Apply prefetch_related
        return Prescription.objects.filter(**filters).prefetch_related(*prefetch_related_objects)
    
    def get_object(self):
        prescription_id = self.kwargs.get('pk')
        if prescription_id is not None:
            return generics.RetrieveUpdateAPIView.get_object(self)
        return None

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
