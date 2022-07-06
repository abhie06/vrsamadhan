from ctypes import addressof
from ctypes.wintypes import PINT
import imp
from multiprocessing import context
from pyexpat.errors import messages
from unittest import registerResult
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import re
from tkinter.messagebox import RETRY
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User, auth
from accc.forms import UserData
from .forms import CreateUserForm
from accc.models import Custom_Approver, Register
from agreement.models import Destination
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user
from .resource import PersonResource
from tablib import Dataset
from django.http import HttpResponse


# Create your views here.


def register(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pan = request.POST.get('pan')        
        gst = request.POST.get('gst')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        pin_code = request.POST.get('pin_code')
        account_number = request.POST.get('account_number')
        ifsc_code = request.POST.get('ifsc_code')
        other = request.POST.get('other')
        service_category = request.POST.get('service_category')
        branch_name = request.POST.get('branch_name')
        agreement_document = request.POST.get('agreement_document')
        pan_document = request.POST.get('pan_document')
        gst_document = request.POST.get('gst_document')
        bank_document = request.POST.get('bank_document')
        other_document = request.POST.get('other_document')
        user = request.user
        approver = request.POST.get('approver')
        register = Register(pan=pan,first_name = first_name,last_name=last_name,email=email,address=address,gst=gst,mobile=mobile,pin_code=pin_code,account_number=account_number,ifsc_code=ifsc_code,other=other,service_category= service_category,branch_name=branch_name,from_date=from_date,to_date=to_date,agreement_document=agreement_document,pan_document=pan_document,gst_document=gst_document,bank_document=bank_document,other_document=other_document,user=user,approver=approver)
        register.save();
        print('User Created')
        return redirect('/')


    else:
        return render(request,'register.html')


@login_required(login_url ='loginPage')
@allowed_users(allowed_roles=['admin'])
def form(request):
    regs = Register.objects.all()
    return render(request,"form.html",{'regs':regs})
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def permission(request):
    perms = Register.objects.all()
    context ={
        'perms' : perms,
    }
    return render(request, "permission.html",context)
@allowed_users(allowed_roles=['admin'])
def appr(request,id):
    perms1 = Register.objects.get(id=id)
    perms1.approved = 1
    perms1.save()
    return redirect('permission')  
@allowed_users(allowed_roles=['admin'])
def disappr(request,id):
    perms1 = Register.objects.get(id=id)
    perms1.approved = 2
    perms1.save()
    return redirect('permission') 
def approve(request):
    perms = Register.objects.all()
    context ={
        'perms' : perms,
    }
    return render(request, "approve.html",context)
def reject(request):
    perms = Register.objects.all()
    context ={
        'perms' : perms,
    }
    return render(request, "reject.html",context)
def show(request, id):
    if request.method == 'POST':
        pi = Register.objects.get(pk=id)
        fm = UserData(request.POST,instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Register.objects.get(pk=id)
        fm = UserData(instance = pi)
    return render(request, 'show.html', {'form':fm})
def choose(request, id):
    perms = Destination.objects.get(pk=1)
    context = {
        'perms' : perms,
    }
    return render(request,'choose.html',context)
def user_registration(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('loginPage')

    context = {'form':form}
    return render(request, "user_registration.html",context)

@unauthenticated_user  
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password=password)
    
       
        if user is not None:
            login(request,user)
            return redirect('welcomePage')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,'loginPage.html',context)
def logoutPage(request):
    logout(request)
    return redirect('loginPage')
@login_required(login_url='loginPage')
def welcomePage(request):
    dests = Destination.objects.all()
    return render(request,"welcomePage.html",{'dests':dests})

def simple_upload(request):
    if request.method =='POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')
        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            value = User(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                
            )
            value.save()
    return render(request,'simple_upload.html')


