
# Create your views here.
from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return render(request,"index.html")
        
def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    contact_from_form = request.POST['Contact']
    comments_from_form = request.POST['Comments']

    context = {
    	"name_on_template" : name_from_form,
    	"location_on_template" : location_from_form,
        "language_on_template" : language_from_form,
    	"contact_on_template" : contact_from_form,
    	"comments_on_template" : comments_from_form,
    }
    return render(request,"show.html",context)


