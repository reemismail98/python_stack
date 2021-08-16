from django.shortcuts import redirect, render, HttpResponse
from .models import Dojo,Ninja
# show all of the data from a table
def index(request):
    context = {
    	"all_the_dojos": Dojo.objects.all(),
        "all_the_ninjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def dojoform(request):
    Dojo.objects.create(name=request.POST['name'],city=request.POST['city'], state=request.POST['state'])

    return redirect("/")    
def ninjaform(request):
    Ninja.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'], dojo_id=request.POST['dojo_id'])
    return redirect("/")    

