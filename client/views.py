from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, Group
from .forms import client_register_form, edit_profile_form_client, booking_form
from .models import client 
from property.models import booking, propertys
from django.contrib.auth import authenticate, login 
from django.utils import timezone
from django.http import HttpResponse

def client_edit_profile(request):
    profile = request.user.client
    form = edit_profile_form_client(instance= profile)
    if request.method == 'POST':
        form = edit_profile_form_client(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'client/client_edit_profile.html', context)

def register_client(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = client_register_form()
    if request.method =='POST':
        form = client_register_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            group, created = Group.objects.get_or_create(name="client")
            group.user_set.add(user)
            group = Group.objects.all()
            
            login(request, user)
            return redirect('client_edit_profile')
        else:
            messages.error(request,'an erorr has occurred during registration')
    context = {'form':form}
  
    return render(request, 'client/client_login_form.html',context)

def client_profile(request):
    profile = request.user.client
    context = {'profile':profile}
    return render(request,'client/client_profile.html',context)

def reservation_propertys(request, pk):
    client_obj = client.objects.get(id=request.user.client.id)
    property_obj = propertys.objects.get(id=pk)
    if request.method == 'POST':
        form = booking_form(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.client = client_obj
            booking_instance.property = property_obj
            booking_instance.save()
            messages.success(request, 'The event property has been reserved.')
            return redirect('propertys_page_NE')
    else:
        form = booking_form()
    
    context = {'form': form, 'property': property_obj}
    return render(request, 'bookings/create_booking.html', context)

def delete_reservation_propertys(request, pk):
    if booking.objects.filter(property=pk).exists():
        booking.objects.filter(property=pk).delete()
        messages.success(request,'reservation property has been deleted')
    else:
        messages.error(request,'error')
    return redirect('propertys_page_NE')
