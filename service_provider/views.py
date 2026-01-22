from django.shortcuts import render, redirect
from .models import service_provider
from .forms import CustomUserCreationForm ,edit_profile_form
from django.contrib.auth import login ,authenticate ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.

def login_form(request):
    page = 'login'
    context = {'page':page}
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username_obj = request.POST['username']
        password_obj = request.POST['password']
        try:
            user = User.objects.get(username=username_obj)
        except:
            messages.error(request,'Username does not exist')
    
        user = authenticate(request, username=username_obj, password=password_obj)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username OR password is incorrect' )
        
    return render(request,'service_provider/service_provider_login_form.html' ,context)

def register_form(request):
    if request.user.is_authenticated:
        return redirect('home')
    page = 'register'
    form = CustomUserCreationForm()
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            group, created = Group.objects.get_or_create(name='service_provider')
            group.user_set.add(user)
            login(request, user)
            return redirect('edit_profile')
        else:
            messages.error(request,'an erorr has occurred during registration')
  
    context = {'page':page ,'form':form}
    return render(request,'service_provider/service_provider_login_form.html',context)
   
def edit_profile(request):
    profile = request.user.service_provider
    form = edit_profile_form(instance= profile)
    if request.method == 'POST':
        form = edit_profile_form(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
            return redirect('service_provider_profile')
    
    context = {'form': form}
    return render(request,'service_provider/srevice_provider_edit_profile.html',context)
    

def logout_form(request):
    logout(request)
    return redirect('login')

def service_provider_page(request):
    service_provider_obj = service_provider.objects.all()
    context = {'service_provider':service_provider_obj}
    return render(request,'service_provider/service_provider_page.html',context)

def service_provider_profile(request):
    profile = request.user.service_provider
    context = {'profile':profile}
    return render(request,'service_provider/service_provider_profile.html',context)