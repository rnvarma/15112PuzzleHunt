from django.shortcuts import render, redirect
from django.views.generic.base import View
from backend.models import *

from backend.models import *

staff_last_names = [
  "Varma","Choo","Benson","Korn","Jiang","O'Niell","Reddy",
  "Bergeron","Frye","Wilson","Kleiven","Yang","Zhang",
  "Liu", "Cong","Shanker","Pintar","Plaut","Qian",
  "Stentz","Schroeder","Morina","Zink","Jadvani","Agrawal",
  "Gakhar","Lao","Shi","Choudary","Damasco","Reichek","Yang",
  "Oshlag","Peraza","Pederson","Fan","Zhang","Kuntz","Zheng",
  "Chhabra","Maines","Eliason","Marinescu","Shnakar"
]

class HomePage(View):

  def get(self, request):
    return render(request, 'homepage.html')

class RegistrationPage(View):

  def post(self, request):
    print dict(request.POST)

  def get(self, request):
    return render(request, 'registration.html')

class PuzzlePage(View):

  def get(self,request):
    context = {}
    puzzles = []
    for puzzle in Puzzle.objects.all():
        obj = puzzle.__dict__
        puzzles.append(obj)
        

    context["puzzles"] = puzzles
    
    return render(request, 'puzzle.html', context)
