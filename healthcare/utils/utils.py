# utils.py
import requests

ACCOUNT_API_HOST = "http://localhost:8002/api/"
APPOINTMENT_API_HOST = "http://localhost:8003/api/"


def get_doctor_list():
    api_endpoint = f"{ACCOUNT_API_HOST}doctors/"
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    return []

def get_patient_list():
    api_endpoint = f"{ACCOUNT_API_HOST}patients/"
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    return []

def get_single_doctor(doctor_id):
    api_endpoint = f"{ACCOUNT_API_HOST}doctors/{doctor_id}/"
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    return None

def get_single_patient(patient_id):
    api_endpoint = f"{ACCOUNT_API_HOST}patients/{patient_id}/"
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    return None


def get_doctor_available_appointment_time(doctor_id,appointment_date):
    api_endpoint = f"{APPOINTMENT_API_HOST}appointment-times/{doctor_id}/{appointment_date}/"
    try:
        response = requests.get(api_endpoint)
        print(response.json())
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    return None
