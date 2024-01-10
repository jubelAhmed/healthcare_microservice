from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.http import HttpResponse
# Create your views here.
class transaction(TemplateView):
    
    template_name = 'apps/payment/home.html'  # Replace with your actual template name

    def post(self, request, *args, **kwargs):
        # Process the form data
        name = request.POST.get('name')
        card_number = request.POST.get('card_number')
        print("Card Number:", card_number)
        card_type = request.POST.get('card_type')
        exp_date = request.POST.get('exp_date')
        cvv = request.POST.get('cvv')
        appointment_id = request.POST.get('appointment_id')
        print(appointment_id)
        patient_id = request.POST.get('patient_id')
        print(patient_id)

        # Perform actions with form data (e.g., process payment, store data in a database)
        # Your logic goes here
        
        # For demonstration purposes, return a success message
        #return HttpResponse("Payment successful! Thank you.")
        return render(request, 'apps/payment/paymentcompleted.html')

