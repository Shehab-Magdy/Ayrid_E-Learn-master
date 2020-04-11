from eLearn.models import ourTeam
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def editTeamMember(request):
    if request.method == 'POST':
        newTeamMember = ourTeam()
        newTeamMember.FullName = request.POST.get('FullName')
        newTeamMember.JobTitle = request.POST.get('JobTitle')
        newTeamMember.description = request.POST.get('description')
        newTeamMember.status = True if request.POST.get('active') else False
        newTeamMember.pic = request.FILES['memberImg']
        newTeamMember.save()
        return render(request, 'admin/adminhome.html')
    elif request.method == 'GET':
        pass
    if ourTeam.objects.all():
        ourteam = ourTeam.objects.all()
    else:
        ourteam=[]
    return render(request, 'admin/adminrotator/ourteam.html', {'ourteam':ourteam})

