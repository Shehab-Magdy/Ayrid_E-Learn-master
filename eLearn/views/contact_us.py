from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.urls import reverse
from django.views.generic import View
from eLearn.models import Registration, HaederSlider
from eLearn.forms import ContactUsForm

def contactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            #send email code goes here
            sender_name = form.cleaned_data['firstName']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a message:\n\n{1}".format(sender_name,form.cleaned_data['message'])
            send_mail('New enquiry',message, sender_email,['enquiry@exampleco.com'])
            return HttpResponse('Thanks for contacting us! ;)')
    else:
        form = ContactUsForm()
    return render(request,'contact_us/contactus.html', {'form': form})
