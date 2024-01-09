from django.shortcuts import render
from django.http import HttpResponse
from utils import utils
from django.shortcuts import render, redirect

import requests

APPOINTMENT_HOST_URL = "http://localhost:8003/api/"

def appointment(request):
    if request.method == 'POST':
        # appointment_id = request.POST.get('appointment_id')
        doctor_id = request.POST.get('doctor_id')
        patient_id = request.POST.get('patient_id')
        appointment_time = request.POST.get('appointment_time')
        appointment_date = request.POST.get('appointment_date')
        purpose = request.POST.get('purpose')
        sick_information = request.POST.get('sick_information')
        obj = {
            "doctor_id": doctor_id,
            "patient_id": patient_id,
            "appointment_time": appointment_time,
            "appointment_date": appointment_date,
            "purpose": purpose,
            "sick_information": sick_information
        }
        print("data", obj)
        response = requests.post(f'{APPOINTMENT_HOST_URL}appointments/', json=obj)
        print("response",response.text)
        if response.status_code == 200:
            print("response 2",response.json())
            return redirect('home')
        else:
            # messages.error(request, 'Appointment creation failed')  
            return redirect('appointment_create')

        # return HttpResponse("Appointment created successfully")
      
    doctor_list = utils.get_doctor_list()
    print("doctor_list", doctor_list)
    context = {
        'doctor_list': doctor_list
    } 
    return render(request, 'apps/appointment/appointment.html', context)

def doctor_view(request):
    return render(request, 'apps/appointment/doctorviews.html', {})

def patient_view(request):
    return render(request, 'apps/appointment/patientviews.html', {})

def appointment_list(request, user_id, user_type):
    try:
        # Define the API endpoint based on user type
        api_url = f"{APPOINTMENT_HOST_URL}{user_type}s/{user_id}/appointments/"

        # Make the GET request to the API
        response = requests.get(api_url)
        print(response.text)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Now 'data' contains the list of appointments from the API
            return render(request, 'apps/appointment/appointment_list.html', {'appointment_list': data})
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
            return HttpResponse("Failed to fetch data from the API", status=response.status_code)
    except requests.RequestException as e:
        # Handle any exception that might occur during the request
        print(f"Request Exception: {e}")
        return HttpResponse("Error during API request", status=500)
    
    
from django.http import JsonResponse

def available_time(request, doctor_id,appointment_date):  
    response_data = utils.get_doctor_available_appointment_time(doctor_id,appointment_date)

    if response_data:
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Failed to fetch available appointment times'}, status=500)