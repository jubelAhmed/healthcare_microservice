# Generated by Django 5.0 on 2024-01-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0002_remove_patient_user_customuser_doctor_specialist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='doctor_specialist',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
