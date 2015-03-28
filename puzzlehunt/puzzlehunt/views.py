from django.shortcuts import render, redirect
from django.views.generic.base import View

class HomePage(View):

  def get(self, request):
    return render(request, 'homepage.html')