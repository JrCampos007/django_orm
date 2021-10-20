from django.shortcuts import render, redirect
from django.db.models.fields import DateField
from django.contrib import messages
from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

def show_details(request, id):      
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request, "show_details.html", context)

def edit(request, id):
    context = {
            "show": Show.objects.get(id=id),
        }
    return render(request, "edit.html", context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST, 'update')
    if len(errors) > 0: 
        for value in errors.values():
            messages.error(request, value)
        print('yeas!')
        return redirect(f'/shows/{id}/edit')
    
    elif request.method == "POST":
        instance = Show.objects.get(id=id)      
        instance.title=request.POST['title']
        instance.network=request.POST['network']
        instance.release_date=request.POST['release_date'] # because by 'release_date' is now set up as "date" on form, I can just assign it directly
        instance.description=request.POST['description']
        instance.save()
        messages.success(request, "Show successfully updated")
    
    return redirect(f'/shows/{id}')


def destroy(request, id):   # ibid on include the "id" here
    instance = Show.objects.get(id=id)      # instantiate
    instance.delete()                       # delete

    return redirect('/')

def new(request):

    return render(request, "new.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST, 'create')
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)

        return redirect('/new')

    elif request.method == "POST":
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        instance = Show.objects.get(title=request.POST['title'])
        messages.success(request, "Show successfully created")

        return redirect(f'/shows/{instance.id}')
    
    return redirect('/shows')

# def title_valid_null(request):
#     # this is just here to deal will null text entry cases
#     found = 3
#     return render(request, 'partials/title.html', {"found":found})


# def title_valid(request, title):
#     list = Show.objects.filter(title = title)
#     print('made it!')
#     found = 2
#     if len(list) > 0:
#         found = 1
#     return render(request, 'partials/title.html', {"found":found})  # found is "like" context and must be a dict datatype
        

# Create your views here.
