from django.shortcuts import render,redirect
from .models import *
from time import strftime
from django.contrib import messages



def index(request):
    context={
        'shows':Show.objects.all(),
    }
    return render(request,"index.html",context)
# Create your views here.
def new_show(request):
    
    return render (request,"new_show.html")

def show_shows_id(request, id):
    context={
            'this_show1': Show.objects.get(id=id),
        }
    return render (request,"tv_show.html",context)

def tv_show(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/shows/new')

    else:
        this_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"],release_date=request.POST["release_date"],description=request.POST['description'])
        context={
            'shows':Show.objects.all(),
            'this_show1': this_show,
                }
        return redirect(f'/shows/{this_show.id}')
    return redirect('/shows/new')

def edit_shows_id(request, id):
    time = Show.objects.get(id=id).release_date
    context={
        'this_edit1': Show.objects.get(id=id),
        'date': time.strftime('%Y-%m-%d')
        }
    return render (request,"edit.html",context)

def update_show(request,id):
    this_edit = Show.objects.get(id=id)

    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        if request.method=="POST":
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect(f'/shows/{this_edit.id}/edit')

    else:
        this_edit.title=request.POST["title"]
        this_edit.network=request.POST["network"]
        this_edit.release_date=request.POST["release_date"]
        this_edit.description=request.POST['description']
        this_edit.save()
        return redirect(f'/shows/{this_edit.id}/edit')

def delete(request,id):
    deletsshow=Show.objects.get(id=id)
    deletsshow.delete()
    return redirect('/shows')



