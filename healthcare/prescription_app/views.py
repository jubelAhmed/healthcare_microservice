# views.py

from django.shortcuts import render
from django.http import HttpResponse
import requests

HOST_URL = "http://127.0.0.1:8005/api"
import logging

logger = logging.getLogger(__name__)

def prescription(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')

        medications = request.POST.getlist('medications[]')  
        medical_tests = request.POST.getlist('medical_tests[]')  
        medication_conditions = request.POST.getlist('medication_conditions[]')  

        # Prepare data for the API request
        prescription_data = {
            'appointment_id': appointment_id,
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            # ... include other prescription data
            'medications': medications,
            'medical_tests': medical_tests,
            'medication_conditions': medication_conditions,
        }

       
        api_url = f"{HOST_URL}/prescriptions/" 
        response = requests.post(api_url, json=prescription_data)

        if response.status_code == 201:  
            return HttpResponse('Prescription created successfully!')
        else:
            return HttpResponse('Failed to create prescription. API returned {}'.format(response.status_code))

    else:
        api_url = f"{HOST_URL}/prescriptions/" 
        response = requests.get(api_url) 
        print("response.status_code")
        print(response.status_code)
        print(response)
        prescription_list = []
        if response.status_code == 200:
            prescription_list = response.json().get('results', [])  # Assuming the data is in JSON format
    
        context = {
            'prescription_list': prescription_list,
        }
        return render(request, 'apps/prescription_app/index.html',context=context)



def update_prescription(request, pk):
    # print("request", request,"pk",pk)
    logger.debug(f"request {request} {pk} pk")

    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('appointment_id')
            patient_id = request.POST.get('patient_id')
            doctor_id = request.POST.get('doctor_id')
            print("appointment_id", appointment_id)

            medications = []
            for i in range(0, int(request.POST.get('medications_count'))):
                medication_name = request.POST.get(f'medicine_name_{i}')
                doses = request.POST.get(f'doses_{i}')
                route = request.POST.get(f'route_{i}')
                frequency = request.POST.get(f'frequency_{i}')
                medication_id = request.POST.get(f'medication_id_{i}',0)

                medications.append({
                    "medicine_name": medication_name,
                     "doses": doses,
                     "route": route,
                     "frequency": frequency,
                     "id": int(medication_id)
                })

            medical_tests = []
            for i in range(0, int(request.POST.get('medical_tests_count'))):
                test_name = request.POST.get(f'test_name_{i}')
                description = request.POST.get(f'description_{i}')
                medical_test_id = request.POST.get(f'medical_test_id_{i}',0)

                medical_tests.append({
                    "test_name": test_name,
                    "description": description,
                    "id": int(medical_test_id)
                })

            medication_conditions = []
            for i in range(0, int(request.POST.get('medication_conditions_count'))):
                condition_name = request.POST.get(f'condition_name_{i}')
                description = request.POST.get(f'description_{i}')
                condition_id = request.POST.get(f'condition_id_{i}',0)

                medication_conditions.append({
                    "id": int(condition_id),
                    "condition_name": condition_name,
                    "description": description,
                })

            # Prepare data for the API request
            prescription_data = {
                "appointment_id": appointment_id,
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "medications": medications,
                "medical_tests": medical_tests,
                "medication_conditions": medication_conditions,
            }
            print("prescription_data")
            print(prescription_data)
            logger.debug(f"prescription_data {prescription_data}")
            api_url = f"{HOST_URL}/prescriptions/{pk}/"
            response = requests.put(api_url, json=prescription_data)
            logger.debug(f"put response {response.text}")
            print("put response", response.status_code, response.text)
            if response.status_code == 200:  
                return HttpResponse('Prescription updated successfully!')
            else:
                return HttpResponse(f'Failed to updated prescription. API returned {response.status_code}')

        except Exception as e:
            print(f"Error processing the prescription form: {e}")
            return HttpResponse('An error occurred while processing the prescription form.')

    else:
        try:
            api_url = f"{HOST_URL}/prescriptions/?id={pk}" 
            response = requests.get(api_url) 
            print("response.status_code")
            print(response.status_code)
            print(response)
            prescription_list = []
            if response.status_code == 200:
                prescription_list = response.json().get('results', [])  # Assuming the data is in JSON format
        
            context = {
                'prescription': prescription_list[0],
            }
            return render(request, 'apps/prescription_app/update.html', context=context)

        except Exception as e:
            print(f"Error retrieving prescription data: {e}")
            return HttpResponse('An error occurred while retrieving prescription data.')