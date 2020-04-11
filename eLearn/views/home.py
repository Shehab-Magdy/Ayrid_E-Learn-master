from eLearn.models import Registration, HaederSlider
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

def index(request):
    if HaederSlider.objects.all():
        a = HaederSlider.objects.all()
        b=[]
        for i in a:
            b.append(i.pic.url)
        data = {'url0': b[0], 'url1': b[1], 'url2': b[2], 'url3': b[3]}
    else:
        data = {'url0': 'http://placekitten.com/g/300/200', 'url1': 'http://placekitten.com/g/300/200', 'url2': 'http://placekitten.com/g/300/200', 'url3': 'http://placekitten.com/g/300/200'}
    return render(request,'home/index.html', {'data':data})
