
from django.http import request
from django.shortcuts import render,redirect
from . import models
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")

def success(request):
    context = {
    	"all_the_users": Users.objects.all(),
        "all_the_messages": Messages.objects.all(),
        "all_the_comments": Comments.objects.all(),
        # 'all_this_message_comments':Comments.objects.filter(Message=Messages.objects.get(id=request.POST['com_id'])),
    }
    # # Check if the user logged in
    if request.session['firstname']:
    #     check_user(request.POST["email"])
        return render(request, 'success.html',context)
    else:
        return redirect('/')

def logout(request):
    request.session.clear
    return redirect("/")   


def registration(request):
    errors = Users.objects.basic_validator(request.POST)
        # check if the errors dictionary has) anything in it
    if errors and len(errors) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/')
    else:
        if request.method=="POST":    
            # if request.POST["login_type"]== "registration":
            # if 'kname' not in request.session:
                request.session["firstname"]=request.POST["firstname"]
                request.session["lastname"]=request.POST["lastname"]
                request.session["email"]=request.POST["email"]
                password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode() 
                register(request.POST["firstname"],request.POST["lastname"],request.POST["email"],password)
                return redirect("/wall")
        return redirect("/")

def login(request):
    errors1 = Users.objects.login_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors1) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors1.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/')
    else:
        user=Users.objects.filter(email=request.POST["email"])
    if user:
        if 'name' not in request.session:
            request.session["id"]=user[0].id
            request.session["firstname"]=user[0].firstname
        logged_user=user[0]   
        if bcrypt.checkpw(request.POST["password"].encode(),logged_user.password.encode()):
            request.session["id"]=logged_user.id
        return redirect("/wall")
             

def postthemessage(request):
    if request.method=="POST":
        request.session["message"]=request.POST["message"]
    #request.session["user_id"]=request.POST["user_id"]
        Messages.objects.create(user_id=Users.objects.get(id=request.session["id"]),message=request.session["message"])  
        messages.success(request,'Message posted successfully.')
        return redirect("/wall")

def postthecomment(request):
    if request.method=="POST":
        request.session["comment"]=request.POST["comment"]
    #request.session["user_id"]=request.POST["user_id"]
        # Comments.objects.create(user_id=Users.objects.get(id=request.session["id"]),message_id=Messages.objects.get(id=request.session["message"]),comment=request.session["comment"])
        Comments.objects.create(user_id=Users.objects.get(id=request.session["id"]),message_id=Messages.objects.get(id=request.POST["com_id"]),comment=request.POST["comment"])

        messages.success(request,'Comment posted successfully.')
        return redirect("/wall")


def deletecomment(request):
    if request.method=="POST":
        c=Comments.objects.get(id=request.POST["del_id"])
        c.delete()
        return redirect("/wall")  
    messages.success(request,'cann’t delete comment.')          

   