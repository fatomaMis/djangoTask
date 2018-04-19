from django.shortcuts import render

from django.conf import settings
from models import Message
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from django.db.models import Max
from django.core.mail import EmailMessage


def index(request):
    return render(request, "index.html", {})

def send(request):
    subject = "New Message"
    message = request.POST['data']
    emailmsg = request.POST['emaildata']
    email = EmailMessage(subject, message, to=[emailmsg])
    email.send()
    return render(request, "index.html", {})
