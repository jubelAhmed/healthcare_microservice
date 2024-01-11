from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView 
from django.http import HttpResponse
import requests
from django.http import JsonResponse

# Create your views here.
class transaction(TemplateView):
    
    template_name = 'apps/payment/home.html'  # Replace with your actual template name

    def get(self, request, appointment_id, patient_id, *args, **kwargs):
        context = {
            'appointment_id': appointment_id,
            'patient_id': patient_id
        }
        return render(request, self.template_name, context)
    
    def post(self, request, appointment_id, patient_id, *args, **kwargs):
        card_number = request.POST.get('card_number')
        expiry_month = request.POST.get('expiry_month')
        expiry_year = request.POST.get('expiry_year')
        cvc = request.POST.get('cvc')
        appointment_id = int(request.POST.get('appointment_id'))
        patient_id = request.POST.get('patient_id')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        url = "http://127.0.0.1:8006/api/make_payment/"
        api_data = {
            "card_number": card_number,
            "expiry_month": expiry_month,
            "expiry_year": expiry_year,
            "cvc": cvc,
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "amount": amount,
            "currency": currency
        }

        # Make the POST request
        api_response = requests.post(url, data=api_data)

        # Check the response from the API
        if api_response.status_code == 200:
            follow_up_url = f"http://127.0.0.1:8003/api/update_payment_status/{appointment_id}/"
            follow_up_data = {
                "appointment_id": appointment_id,
                "payment_status": "success"
            }

            # Make the follow-up request
            follow_up_response = requests.post(follow_up_url, json=follow_up_data)
            print("follow_up_response 1")
            print(follow_up_response.text)
            print(follow_up_response.status_code)
            # Check the response from the follow-up API
            if follow_up_response.status_code == 200:
               return redirect('appointment_list', user_id=patient_id, user_type='patient')
            else:
                return JsonResponse({"error": "Failed to check payment status"}, status=500)
            
        else:
            return HttpResponse(f"Transaction Failed! Try to create a new appointment")
        
