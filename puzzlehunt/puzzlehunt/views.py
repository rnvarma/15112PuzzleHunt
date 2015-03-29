from django.shortcuts import render, redirect
from django.views.generic.base import View

from backend.models import *

class HomePage(View):

  def get(self, request):
    return render(request, 'homepage.html')

class RegistrationPage(View):

  def get(self, request):
    return render(request, 'registration.html')
