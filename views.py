from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse

from .models import *


def subscrib(request, pk):
    subscriber = request.user.email
    category = Subscribers.object.filter(id=pk)
    category.subscribers.add(subscriber)

    return HttpResponse(f'{subscriber}')