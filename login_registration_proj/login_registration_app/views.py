from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration
import bcrypt   

# Create your views here.
def index(request):
    request.session.flush()
    return render(request, "login_reg.html")

def create_user(request):
    if request.method == "POST":
        errors = Registration.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')

        print(request.POST['password'])
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hashed_pw)

        user1 = Registration.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_pw,
        )
        request.session['user_id'] = user1.id
        return redirect('/success')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = Registration.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0]
    }
    return render(request, 'dashboard.html', context)

def login_user(request):
    if request.method == "POST":
        errors = Registration.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        this_user = Registration.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')