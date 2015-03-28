from django.db import models
from django.conf import settings

class TeamData(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL)
  levels_solved = models.CharField(default="", max_length=100)

  puzzle1_score = models.IntegerField(default=0)
  puzzle2_score = models.IntegerField(default=0)
  puzzle3_score = models.IntegerField(default=0)
  puzzle4_score = models.IntegerField(default=0)
  puzzle5_score = models.IntegerField(default=0)

  puzzle1_started = models.DateTimeField(blank=True, null=True)
  puzzle2_started = models.DateTimeField(blank=True, null=True)
  puzzle3_started = models.DateTimeField(blank=True, null=True)
  puzzle4_started = models.DateTimeField(blank=True, null=True)
  puzzle5_started = models.DateTimeField(blank=True, null=True)

  puzzle1_completed = models.DateTimeField(blank=True, null=True)
  puzzle2_completed = models.DateTimeField(blank=True, null=True)
  puzzle3_completed = models.DateTimeField(blank=True, null=True)
  puzzle4_completed = models.DateTimeField(blank=True, null=True)
  puzzle5_completed = models.DateTimeField(blank=True, null=True)

  puzzle1_hintsused = models.IntegerField(default=0)
  puzzle2_hintsused = models.IntegerField(default=0)
  puzzle3_hintsused = models.IntegerField(default=0)
  puzzle4_hintsused = models.IntegerField(default=0)
  puzzle5_hintsused = models.IntegerField(default=0)


class Puzzle(models.Model):
  answer = models.CharField(default="", max_length=100)
  puzzle_unlocked = models.BooleanField(default=False)

  hint1 = models.TextField(default="")
  hint2 = models.TextField(default="")
  hint3 = models.TextField(default="")
  hint4 = models.TextField(default="")
  hint5 = models.TextField(default="")

  hint1_unlocked = models.BooleanField(default=False)
  hint2_unlocked = models.BooleanField(default=False)
  hint3_unlocked = models.BooleanField(default=False)
  hint4_unlocked = models.BooleanField(default=False)
  hint5_unlocked = models.BooleanField(default=False)



