from argparse import ONE_OR_MORE, ArgumentDefaultsHelpFormatter
from cProfile import label
from calendar import c
from curses.ascii import US
from distutils.command.upload import upload
from email.policy import default
from enum import unique
from importlib.metadata import requires
from sre_constants import MAX_REPEAT
from statistics import mode
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User,Group
from datetime import datetime,date
from django.core.validators import RegexValidator

import re

from django.forms import CharField

ADVERTISMENT = 'AD'
CONSULTANCY = 'CN'
SUPPORT_SERVICE = 'SR'
RENT = 'RT'
CHOICE = (
    (ADVERTISMENT,"Advertisment"),
    (CONSULTANCY, "Consultancy"),
    (SUPPORT_SERVICE,"Service"),
    (RENT,"Rent"),
)
AHMEDABAD = 'AB'
BOMBAY = 'BO'
SHIMLA = 'SH'
CHOICE_ = (
    (AHMEDABAD, "Ahmedabad"),
    (BOMBAY, "Bombay"),
    (SHIMLA, "SHIMLA")
)
A = 'A'
B = 'B'
C = 'C'
D = 'D'
CHOICE__ = (
    
(A,"A"),
    (B,"B"),
    (C,"C"),
    (D,"D")


)
PHONE_NUMBER_REGEX = RegexValidator(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', 'Enter Valid Pan Card Number')

# Create your models here.
class Register(models.Model):  
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25,blank=False)
    pan =models.CharField(max_length=10,  validators=[PHONE_NUMBER_REGEX], unique=True,blank=False)
    gst = models.CharField(max_length=15)
    address = models.CharField(max_length=254)
    mobile = models.IntegerField()
    pin_code = models.IntegerField()
    account_number = models.IntegerField()
    ifsc_code = models.IntegerField()
    other = models.CharField(max_length=254)
    service_category = models.CharField (
        max_length=254,
        choices= CHOICE,
        default= ADVERTISMENT,
    )
    branch_name = models.CharField(
        max_length= 254,
        choices = CHOICE_,
        default = AHMEDABAD,
    )
    from_date = models.DateField(auto_now_add=False,auto_now=False,blank=False)
    to_date = models.DateField(auto_now_add=False,auto_now= False, blank= False )
    agreement_document = models.ImageField(upload_to="pics/images",default="")
    pan_document = models.ImageField(upload_to="pics/images",default="")
    gst_document = models.ImageField(upload_to="picsimages",default="")
    bank_document = models.ImageField(upload_to="pics/images",default="")
    other_document = models.ImageField(upload_to="pics/images",default="")
    approved = models.IntegerField(null=True, default=0)
    user = models.CharField(max_length=255, null = True)
    approver = models.CharField(
        max_length=254,
        choices= CHOICE_,
        default= 'A'

    )


class Custom_Approver(models.Model):
    claim = models.OneToOneField(Register,null= True, on_delete=models.CASCADE)
    approver1 = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    reason1 = models.CharField(max_length=254)
    approver2 = models.OneToOneField(User, related_name='%(class)s_requests_created',null=True,on_delete=models.CASCADE)
    reason2 = models.CharField(max_length=254)
    






    
