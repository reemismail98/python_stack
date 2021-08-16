
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
        "all_the_thought": Thoughts.objects.all(),

      
        }
        
    
    # # Check if the user logged in
    return render(request, 'success.html',context)
    
   

def logout(request):
    request.session.clear()
    return redirect("/")   


def registration(request):
    errors = Users.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if errors and len(errors) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/')
    else:
        if request.method=="POST":
            password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode() 
            user = register(request.POST["firstname"],request.POST["lastname"],request.POST["email"],password)    
            request.session["id"]= user.id
            request.session["firstname"]=user.firstname
            request.session["lastname"]=user.lastname
            request.session["email"]=user.email
            return redirect("/thoughts")
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
        logged_user=user[0]   
        if bcrypt.checkpw(request.POST["password"].encode(),logged_user.password.encode()):
            request.session["id"]=logged_user.id
            request.session["firstname"]=logged_user.firstname
        return redirect("/thoughts")

def postthethought(request):
    if request.method=='POST':
        errors = Thoughts.objects.post_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/thoughts")
        else:
            
            Thoughts.objects.create(user_uploaded=Users.objects.get(id=request.session["id"]),textthought=request.POST["thought"])  
            # messages.success(request,'Thought posted successfully.')
            return redirect("/thoughts")

             
def deletethought(request):
    this_thought=Thoughts.objects.get(id=request.POST["del_id"])
    this_thought.delete()
    return redirect("/thoughts")  



def detalies(request,id):
    context={
        "all_the_thought": Thoughts.objects.all(),

        "this_thought":Thoughts.objects.get(id=id),
        "all_the_user": Users.objects.all(),
    }
  
    return render(request, 'detalies.html',context)



def addthought(request,id):
    adduser=request.session["id"]
    addthought= Thoughts.objects.get(id=id)
    addthought.user_liked.add(adduser)
    
    return redirect("/thoughts/"+str(id))

def removethought(request,id):
    adduser=request.session["id"]
    addthought= Thoughts.objects.get(id=id)
    addthought.user_liked.remove(adduser)
    
    return redirect("/thoughts/"+str(id))    