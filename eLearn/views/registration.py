from eLearn.models import Registration
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def newRegistration(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phone')
        fullname = request.POST.get('fullname')
        birthdate = request.POST.get('birthdate')
        profileimage = request.FILES['profileimage']
        newreg = Registration()
        newreg.email = email
        newreg.password = password
        newreg.phoneNumber = phoneno
        newreg.fullName = fullname
        newreg.birthDate = birthdate
        newreg.Profilephoto = profileimage
        newreg.save()
        return render(request, 'registration/login.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    elif request.method == 'POST':
        ema = request.POST.get('email')
        passw = request.POST.get('password')
        try:
            logedinUser = Registration.objects.get(email=ema , password=passw)
            return render(request, 'home/index.html')
        except Registration.DoesNotExist:
            return HttpResponse('Email or Password is incorrect')
