from eLearn.models import Registration
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

def about(request):
    return render(request,'about_us/about.html')
