from eLearn.models import Registration, HaederSlider
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def saveRotator(request):
    names = ['1st_slide','2nd_slide','3rd_slide','4th_slide']
    if request.method == 'POST':
        if HaederSlider.objects.all():
            st = HaederSlider.objects.get(name=names[0])
            nd = HaederSlider.objects.get(name=names[1])
            rd = HaederSlider.objects.get(name=names[2])
            th = HaederSlider.objects.get(name=names[3]) 
            st.pic = request.FILES[names[0]]
            nd.pic = request.FILES[names[1]]
            rd.pic = request.FILES[names[2]]
            th.pic = request.FILES[names[3]]
            st.save()
            nd.save()
            rd.save()
            th.save()
        else:
            for n in names:
                HaederSlider.objects.create(name = n,pic = request.FILES[n])
        return redirect(reverse('eLearn:elearn.admin'))
    elif request.method == 'GET':
        if HaederSlider.objects.all():
            a = HaederSlider.objects.all()
            b=[]
            for i in a:
                b.append(i.pic.url)
            data = {'url0': b[0], 'url1': b[1], 'url2': b[2], 'url3': b[3]}
        else:
            data = {'url0': 'http://placekitten.com/g/300/200', 'url1': 'http://placekitten.com/g/300/200', 'url2': 'http://placekitten.com/g/300/200', 'url3': 'http://placekitten.com/g/300/200'}
        return render(request, 'admin/adminrotator/rotator.html', {'data':data})
