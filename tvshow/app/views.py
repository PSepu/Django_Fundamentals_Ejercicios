from django.shortcuts import render, redirect, reverse
from app.models import Show

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request,"index.html")
    if request.method == "POST":
        print(request.POST)
        return redirect("/")

def create(request):
    if request.method == "GET":
        return render(request, 'create_show.html')
    if request.method == "POST":
        print(request.POST)
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        
        Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
        return redirect("all_shows")

def all_shows(request):
    if request.method == "GET":
        contexto = {
            'shows': Show.objects.all().order_by('-updated_at'),
        }
        return render(request, 'all_shows.html', contexto)

def show(request, id):
    if request.method == "GET":
        contexto = {
            'show': Show.objects.get(id=id)
        }
        return render(request, 'show.html', contexto)

def edit(request, id):
    
    show = Show.objects.get(id=id)

    if request.method == 'GET':
        contexto = {
            'show' : show
        }
        return render(request, 'edit.html',contexto)
    
    if request.method == "POST":
        print(request.POST)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']  
        show.save()
        
    return redirect(reverse('all_shows'))

def delete(request, id):
    show = Show.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'show' : show
        }
        return render(request,'confirm_delete.html', contexto)
    if request.method == 'POST':
        show.delete()
    return redirect(reverse('all_shows'))