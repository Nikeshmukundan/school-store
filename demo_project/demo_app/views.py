from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Course

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword :
            if not username or not password or not cpassword:
                # Handle empty fields
                return render(request, 'login.html', {'error': 'All fields are required'})

                # Further validation logic
            if password != cpassword:
                # Handle password mismatch
                return render(request, 'login.html', {'error': 'Passwords do not match'})
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('demo_app:register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('demo_app:login')
        else:
            messages.info(request, "password does not match")
            return redirect('demo_app:register')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("login")
            return redirect('demo_app:person_add')
        else:

            messages.info(request,"invalid credentials")
            return redirect('demo_app:login')
            print("error")
    return render(request,'login.html')
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'city_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
def logout(request):
    auth.logout(request)
    return redirect('demo_app:index')