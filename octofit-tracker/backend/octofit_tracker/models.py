from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=24)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24, null=True, blank=True)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    user_id = models.CharField(max_length=24)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    distance = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    user_id = models.CharField(max_length=24)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    user_id = models.CharField(max_length=24)
    score = models.IntegerField()
