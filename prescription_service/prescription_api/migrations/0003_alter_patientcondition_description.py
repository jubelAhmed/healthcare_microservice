# Generated by Django 5.0 on 2024-01-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription_api', '0002_alter_patientcondition_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientcondition',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
