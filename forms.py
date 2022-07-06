from import_export import resources
from django.core import validators
from django import forms
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class UserData(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name','last_name','email' ,'pan','gst','address','mobile' ,'pin_code','account_number','ifsc_code','other','service_category','branch_name','from_date','to_date','agreement_document','pan_document',
    'gst_document',
    'bank_document',
    'other_document',]
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class PersonData(forms.Form):
    class Meta:
        model = User
        fields = '__all__'


