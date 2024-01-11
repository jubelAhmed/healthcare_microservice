from django.db import models

# Create your models here.


from django.db import models

class Appointment(models.Model):
    doctor_id = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=50)
    appointment_time = models.CharField(max_length=50,choices=[('09:00', '9:00 AM'), ('09:20', '9:20 AM'), ('09:40', '9:40 AM'),
                                                  ('10:00', '10:00 AM'), ('10:20', '10:20 AM'), ('10:40', '10:40 AM'),
                                                  ('11:00', '11:00 AM'), ('11:20', '11:20 AM'), ('11:40', '11:40 AM'),
                                                  ('12:00', '12:00 PM'), ('12:20', '12:20 PM'), ('12:40', '12:40 PM'),
                                                  ('13:00', '1:00 PM'), ('13:20', '1:20 PM'), ('13:40', '1:40 PM'),
                                                  ('14:00', '2:00 PM')],
                                       default='09:00')
    appointment_date = models.DateField()
    purpose = models.TextField()
    sick_information = models.TextField()
    PAYMENT_STATUS_CHOICES = [
        ('failed', 'Failed'),
        ('success', 'Success'),
    ]

    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='failed',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

