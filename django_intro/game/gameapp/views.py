from django.shortcuts import render, redirect
import datetime
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity']=[]
    return render(request, 'index.html')

def process_money(request):
    if request.method=="POST":
        gold=0
        if request.POST['farm'] == 'farm':
            gold=random.randint(10, 20)
            request.session['activity'].append('You are Earned '+str(gold)+'golds form the Farm ('+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())) 
        elif request.POST['farm'] == 'cave':
            gold=random.randint(5, 10)
            request.session['activity'].append('You are Earned '+str(gold)+'golds form the Cave('+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
        elif request.POST['farm'] == 'house':
            gold= random.randint(2, 5)
            request.session['activity'].append('You are Earned '+str(gold)+'golds form the House('+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
        elif request.POST['farm'] == 'casino':
            gold= random.randint(-50, 50)
            if gold>=0:
                request.session['activity'].append('Earned a casino and earned '+str(gold)+'golds ('+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            else:
                request.session['activity'].append('Entered a casino and lost '+str(gold)+'golds form the Casino('+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
        request.session['gold']+=gold

    return redirect('/')

def reset(request):
    
    request.session.clear()

    return redirect('/')
    
