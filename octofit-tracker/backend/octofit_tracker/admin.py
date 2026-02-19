from django.contrib import admin
from .models import User, Team, Activity, Workout, Leaderboard

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'team_id')
    search_fields = ('username', 'email')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'type', 'duration', 'distance', 'timestamp')
    search_fields = ('user_id', 'type')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'date')
    search_fields = ('user_id', 'name')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'score')
    search_fields = ('user_id',)
