
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
import uuid

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel_id = str(uuid.uuid4().hex[:24])
        dc_id = str(uuid.uuid4().hex[:24])
        marvel = Team.objects.create(id=marvel_id, name='Marvel')
        dc = Team.objects.create(id=dc_id, name='DC')

        # Create users
        ironman_id = str(uuid.uuid4().hex[:24])
        captain_id = str(uuid.uuid4().hex[:24])
        batman_id = str(uuid.uuid4().hex[:24])
        superman_id = str(uuid.uuid4().hex[:24])
        ironman = User.objects.create(id=ironman_id, username='ironman', email='ironman@marvel.com', password='password', team_id=marvel_id)
        captain = User.objects.create(id=captain_id, username='captain', email='captain@marvel.com', password='password', team_id=marvel_id)
        batman = User.objects.create(id=batman_id, username='batman', email='batman@dc.com', password='password', team_id=dc_id)
        superman = User.objects.create(id=superman_id, username='superman', email='superman@dc.com', password='password', team_id=dc_id)

        # Create activities
        Activity.objects.create(id=str(uuid.uuid4().hex[:24]), user_id=ironman_id, type='run', duration=30, distance=5)
        Activity.objects.create(id=str(uuid.uuid4().hex[:24]), user_id=batman_id, type='cycle', duration=60, distance=20)

        # Create workouts
        Workout.objects.create(id=str(uuid.uuid4().hex[:24]), user_id=ironman_id, name='Chest Day', description='Bench press and pushups')
        Workout.objects.create(id=str(uuid.uuid4().hex[:24]), user_id=superman_id, name='Leg Day', description='Squats and lunges')

        # Create leaderboard
        Leaderboard.objects.create(id=str(uuid.uuid4().hex[:24]), user_id=ironman_id, score=100)
        Leaderboard.objects.create(id=str(uuid.uuid4().hex[:24]), user_id=superman_id, score=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
