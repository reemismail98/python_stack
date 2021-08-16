from django.shortcuts import HttpResponse, redirect 
from django.http import JsonResponse

def root(request):
    return redirect("/index")

def new(request):
    return HttpResponse('placeholder to later display a list of all blogs ')

def edit(request,number):
    return HttpResponse('placeholder to later display a list of all blogs '+number)

def destroy(request,number):
    return redirect("/new")

def create(request):
    return redirect('/')
def emptyroot(request):
    return HttpResponse('in the root')





def index(request):
    return HttpResponse('placeholder to later display a list of all blogs ')
