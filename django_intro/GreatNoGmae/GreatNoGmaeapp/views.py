from django.shortcuts import render, redirect
import random
def index(request):
    if 'num' not in request.session:
        request.session['num'] = random.randint(1, 100)
    if 'no' in request.POST.keys() and request.POST['no']:
        if int(request.POST['no']) < request.session['num']:
            request.session['text']= "Too Low"
        elif int(request.POST['no'])>request.session['num']:
            request.session['text']= "Too High"
        else:
            request.session['text']='Correct'
    return render(request, 'index.html')


