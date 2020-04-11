from eLearn.models import Members
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def editMembers(request):
    if request.method == 'POST':
        newMember = Members()
        newMember.FullName = request.POST.get('FullName')
        newMember.description = request.POST.get('description')
        newMember.status = True if request.POST.get('active') else False
        newMember.pic = request.FILES['memberImg']
        newMember.save()
        return render(request, 'admin/adminhome.html')
    elif request.method == 'GET':
        pass
    if Members.objects.all():
        members = Members.objects.all()
    else:
        members=[]
    return render(request, 'admin/adminrotator/members.html', {'members':members})

