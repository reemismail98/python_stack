from django.shortcuts import redirect, render, HttpResponse
from .models import Users
# show all of the data from a table
def index(request):
    context = {
    	"all_the_users": Users.objects.all()
    }
    return render(request, "index.html", context)

def userform(request):
    Users.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], age=request.POST['age'])
    return redirect("/")    
