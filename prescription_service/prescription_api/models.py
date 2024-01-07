from django.db import models


class Prescription(models.Model):
    appointment_id = models.IntegerField(unique=True)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ['appointment_id', 'patient_id', 'doctor_id']
    def __str__(self):
        return f"Prescription for Appointment ID: {self.appointment_id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id} at {self.created_at}"

class Medication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    doses = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)

class MedicalTest(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    description = models.TextField()

class PatientCondition(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    condition_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
