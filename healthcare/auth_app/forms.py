# frontend_app/forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    phone = forms.CharField(label='Phone', max_length=10,required=False)
    age = forms.IntegerField(label='Age',required=False)
    address = forms.CharField(label='Address', max_length=255,required=False)
    city = forms.CharField(label='City', max_length=100,required=False)
    Country = forms.CharField(label='Country', max_length=100,required=False)
    postcode = forms.CharField(label='Postcode', max_length=10,required=False)
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    gender_choices = [('0', 'Male'), ('1', 'Female'), ('2', 'Other')]
    gender = forms.ChoiceField(label='Gender', choices=gender_choices,required=False)
    user_type_choices = [('doctor', 'Doctor'), ('patient', 'Patient')]
    user_type = forms.ChoiceField(label='User Type', choices=user_type_choices, widget=forms.RadioSelect)
    doctor_specialist = forms.CharField(label='Doctor Specialist', max_length=100, required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')  # Updated to EmailField
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
