from django.shortcuts import render, redirect
from django.views.generic.base import View
from backend.models import *

from backend.models import *

class HomePage(View):

  def get(self, request):
    return render(request, 'homepage.html')

class RegistrationPage(View):

  def get(self, request):
    return render(request, 'registration.html')

class PuzzlePage(View):

  def get(self,request):
    context = {}
    puzzles = Puzzle.objects.all()
    
    return render(request, 'puzzle.html', context)
