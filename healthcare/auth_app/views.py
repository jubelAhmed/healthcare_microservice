from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# frontend_apps/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
import requests
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import logout
from django.conf import settings
from datetime import datetime

AUTH_HOST_API = "http://127.0.0.1:8002/api"

class RegistrationView(View):
    template_name = 'apps/auth/registration.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'apps/auth/registration.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('Country')
        postcode = request.POST.get('postcode')
        dob = request.POST.get('dob')
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
            dob = dob_date.isoformat()
        except ValueError:
            # Handle the case where the provided date is not in the expected format
            # You may want to return an error response or set dob_string to None based on your use case
            dob = ""
        gender = request.POST.get('gender')

        # Additional logic based on user_role
        user_role = request.POST.get('user_role')
        is_doctor = user_role == 'doctor'
        is_patient = user_role == 'patient'

        if is_patient:
            doctor_specialist = ''  # Set doctor_specialist to empty for patients
        else:
            doctor_specialist = request.POST.get('doctor_specialist')

        password = request.POST.get('password')

        data = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'age': age,
            'address': address,
            'city': city,
            'Country': country,
            'postcode': postcode,
            'dob': dob,
            'gender': gender,
            'is_doctor': is_doctor,
            'is_patient': is_patient,
            'doctor_specialist': doctor_specialist,
            'password': password,
        }
        print("data",data)
        response = requests.post(f'{AUTH_HOST_API}/register/', json=data)
        print("response",response.json())
        if response.status_code == 200:
            request.session['user_id'] = response.json()['user_id']
            request.session['user_type'] = response.json()['user_type']
            request.session['access_token'] = response.json()['access']
            return redirect('home')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')  
            return render(request, 'apps/auth/login.html')


class HomeView(View):
    def get(self, request):
        if 'access_token' in request.session:
            return render(request, 'main_home.html')
        else:
            return redirect('login')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'apps/auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post(f'{AUTH_HOST_API}/login/', data=data)
            print(response.json())
            if response.status_code == 200:
                # Store the access token in the session or cookie for future requests
                data = response.json()
                request.session['access_token'] = data['access']
                request.session['user_id'] = data['user_id']
                request.session['user_type'] = data['user_type']
                return redirect('home')
            else:
                messages.error(request, 'Login failed. Please check your credentials.')
        return render(request, 'apps/auth/login.html', {'form': form})
        
class ProfileView(View):
    def get(self, request):
        if 'access_token' in request.session:
            return render(request, 'profile.html')


class LogoutView(View):
    def get(self, request):
        if 'access_token' in request.session:
            del request.session['access_token']
            logout(request)
        return redirect('login')

