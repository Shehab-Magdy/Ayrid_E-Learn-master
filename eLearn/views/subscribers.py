from eLearn.models import SiteSubscribers
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def editSubscribers(request):
    if request.method == 'POST':
        newTeamMember = SiteSubscribers()
        newTeamMember.email = request.POST.get('email')
        newTeamMember.status = True if request.POST.get('active') else False
        newTeamMember.save()
        return redirect(reverse('eLearn:elearn.home'))
    elif request.method == 'GET':
        pass
    if SiteSubscribers.objects.all():
        subscribers = SiteSubscribers.objects.all()
    else:
        subscribers=[]
    return redirect(reverse('eLearn:elearn.admin'), {'subscribers':subscribers})#render(request, 'elearn.home', {'subscribers':subscribers})
    
