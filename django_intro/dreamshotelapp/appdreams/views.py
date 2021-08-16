from django.http import request
from django.shortcuts import render,redirect
from . import models
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")  

def rooms2(request):
    errors = Customer.objects.login_validator(request.POST)
        # check if the errors dictionary has) anything in it
    if len(errors) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/')
    else:
        if request.method=="POST": 
            check_in=request.POST["check_in"]
            check_in=request.POST["check_out"]
            adults=request.POST["adults"]
            # new_reserv=models.create_booking(first_name,last_name,email,phone)
            return redirect('/rooms')

def rooms(request):
        return render(request,"rooms.html")              

def cards(request):
    return render(request,"checkout.html")    

def cards2(request):
    errors = Customer.objects.basic_validator(request.POST)
        # check if the errors dictionary has) anything in it
    if len(errors) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/cards')
    else:
        if request.method=="POST": 
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            phone=request.POST['mobile']
            # new_reserv=models.create_booking(first_name,last_name,email,phone)
            return redirect('/voucher')

def voucher(request):
    return render(request,"voucher.html")        

