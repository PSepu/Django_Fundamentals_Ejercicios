from django.shortcuts import render, redirect
import random
from time import localtime, strftime, time

def index(request):
    return render(request, 'ninjaapp/index.html')

def money(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold']=0
        request.session['activities']=[]
    if request.method == 'POST':
        activities = []
        total_gold = 0
        if request.POST['building'] == 'farm':
            gold = random.randint(10, 21)
            request.session['total_gold'] += gold
            activities.append(' Earned '+str(gold)+' gold from the '+ request.POST['building'] +' - '+ strftime("%Y-%m-%d %H:%M %p", localtime()))
        elif request.POST['building'] == 'cave':
            gold = random.randint(5,11)
            request.session['total_gold'] += gold
            activities.append('Earned '+str(gold)+' gold from the '+ request.POST['building'] +' - '+ strftime("%Y-%m-%d %H:%M %p", localtime()))
        elif request.POST['building'] == 'house':
            gold = random.randint(2,6)
            request.session['total_gold'] += gold
            activities.append('Earned '+str(gold)+' gold from the '+ request.POST['building'] +' - '+ strftime("%Y-%m-%d %H:%M %p", localtime()))
        elif request.POST['building'] == 'casino':
            gold = random.randint(-50,51)
            request.session['total_gold'] += gold
            if gold > 0:
                activities.append('Earned '+str(gold)+' gold from the '+ request.POST['building'] +' - '+ strftime("%Y-%m-%d %H:%M %p", localtime()))
            else:
                activities.append('Lost'+str(gold)+' gold from the '+ request.POST['building'] +' - '+ strftime("%Y-%m-%d %H:%M %p", localtime()))
        
        if 'activities' not in request.session:
            request.session['activities'] = []
        else:
            request.session['activities'] += activities

    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return redirect('/')
