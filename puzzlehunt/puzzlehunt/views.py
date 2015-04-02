from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import (HttpResponse, HttpResponseNotFound,
    HttpResponseBadRequest, HttpResponseServerError,
    HttpResponseRedirect)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from backend.models import *
import random

staff_last_names = set([
  "Varma","Choo","Benson","Korn","Jiang","O'Niell","Reddy",
  "Bergeron","Frye","Wilson","Kleiven","Yang","Zhang",
  "Liu", "Cong","Shanker","Pintar","Plaut","Qian",
  "Stentz","Schroeder","Morina","Zink","Jadvani","Agrawal",
  "Gakhar","Lao","Shi","Choudary","Damasco","Reichek","Yang",
  "Oshlag","Peraza","Pederson","Fan","Zhang","Kuntz","Zheng",
  "Chhabra","Maines","Eliason","Marinescu","Shnakar"
])

def login_user(request):
  username = password = ''
  if request.POST:
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect('/')
  return HttpResponseRedirect("/login")

def logout_user(request):
  logout(request)
  return HttpResponseRedirect("/login")

class HomePage(View):

  def get(self, request):
    return render(request, 'homepage.html')

class RegistrationPage(View):

  def get_unique_team_name(self):
    teams = TeamData.objects.all()
    used_names = set([x.team_name for x in teams])
    unused_names = staff_last_names - used_names
    return random.choice(list(unused_names))

  def post(self, request):
    post_data = dict(request.POST)
    pw = post_data["password"][0]
    members = []
    for i in xrange(1, 5):
      field = "member" + str(i)
      members.append(post_data[field][0])
    team_name = self.get_unique_team_name()
    user = User.objects.create_user(team_name, "", pw)
    user.save()
    ud = TeamData(user=user, member1=members[0], member2=members[1],
      member3=members[2], member4=members[3], team_name=team_name)
    ud.save()
    user_login = authenticate(username=team_name, password=pw)
    login(request, user_login)
    return HttpResponse("")

  def get(self, request):

    return render(request, 'registration.html', {"user": request.user})

class PuzzlePage(View):

  def get(self,request):
    context = {}
    puzzles = []
    for puzzle in Puzzle.objects.all():
        obj = puzzle.__dict__
        puzzles.append(obj)
    context["puzzles"] = puzzles
    return render(request, 'puzzle.html', context)

class IndividualPuzzlePage(View):

  def get(self, request, p_id):
    p_id = int(p_id)
    if p_id > 5:
      return HttpResponseRedirect("/puzzles")
    context = {}
    puzzle = Puzzle.objects.get(number = p_id)
    context["puzzle"] = puzzle.__dict__
    return render(request, 'puzzles/%d.html' % p_id, context)

class LoginPage(View):

  def get(self, request):
    return render(request, 'login.html')
