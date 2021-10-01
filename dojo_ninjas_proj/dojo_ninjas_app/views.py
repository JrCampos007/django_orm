from django.shortcuts import redirect, render
from .models import Ninja, Dojo

def index(request):
    context = {
        "all_ninjas": Ninja.objects.all(),
        "all_dojos": Dojo.objects.all(),
    }

    return render(request, "index.html", context)

def add_dojo(request):      # POST request triggered by Form Action "add_dojo" on index.html; next step is to Create db record:
    if request.method == "POST":
        Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])

    return redirect('/')

def add_ninja(request):     # POST request trig by Form Action "add_ninja" on index.html; create db record: 
    if request.method == "POST":
        instance = Dojo.objects.get(id=request.POST['dojo'])    
        Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=instance)

    return redirect('/')

def delete_dojo(request):   # POST request trig by Form Action "delete_dojo" on index.html; works because "submit" button and "hidden" field type sends the dojo.id
    if request.method == "POST":
        instance = Dojo.objects.get(id=request.POST['dojoID'])  
        instance.delete()                                       

    return redirect('/')

# Create your views here.
