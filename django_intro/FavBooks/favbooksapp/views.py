
from django.http import request
from django.shortcuts import render,redirect
from . import models
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")

def books(request):
    context = {
    	"all_the_users": Users.objects.all(),
        "all_the_books": Books.objects.all(),
        'logged_user':Users.objects.get(id=request.session['id'])
        
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
                return redirect("/books")
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
        return redirect("/books")


def addbook(request):
    errors = Books.objects.basic_validator(request.POST)
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
            Books.objects.create(title=request.POST["title"],desc=request.POST["desc"],uploded_by=Users.objects.get(id=request.session["id"]))
            useradding=Users.objects.get(id=request.session["id"])
            useradding.favbook.add(Books.objects.last())
            return redirect("/books")

def favbook(request,idb,idu):
    this_book = Books.objects.get(id=idb)	# retrieve an instance of a book
    this_publisher = Users.objects.get(id=idb)   
    this_publisher.favbook.add(this_book) 
    return redirect("/books")

def showbook(request,id):
    boo=Books.objects.get(id=id)
    user = Users.objects.filter(email=request.session['email'])
    context = {
    
    	"all_the_users": Users.objects.all(),
        "all_the_books": boo,
        'logged_user':user[0],
        "book_liked_by":models.book_liked_by(request.session['id'],id)
        
    }
    return render(request,'showbook.html',context)
         

   