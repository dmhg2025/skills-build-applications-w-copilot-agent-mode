from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(id='testid', name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(id='testid2', name='Test Team 2')
        user = User.objects.create(id='testuser', username='test', email='test@example.com', team_id=team.id)
        self.assertEqual(user.username, 'test')

    def test_activity_create(self):
        user = User.objects.create(id='testuser2', username='test2', email='test2@example.com')
        activity = Activity.objects.create(id='act1', user_id=user.id, type='run', duration=10, distance=1.5)
        self.assertEqual(activity.type, 'run')

    def test_workout_create(self):
        user = User.objects.create(id='testuser3', username='test3', email='test3@example.com')
        workout = Workout.objects.create(id='wo1', user_id=user.id, name='Pushups', description='Do pushups')
        self.assertEqual(workout.name, 'Pushups')

    def test_leaderboard_create(self):
        user = User.objects.create(id='testuser4', username='test4', email='test4@example.com')
        lb = Leaderboard.objects.create(id='lb1', user_id=user.id, score=50)
        self.assertEqual(lb.score, 50)
