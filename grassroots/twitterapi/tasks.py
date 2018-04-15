from celery import task
from celery.schedules import crontab
from grassroots.celery import app
from . import services
from .models import Status
from ppcwrapper.models import CongressMember
from .serializers import StatusSerializer

app.conf.beat_schedule = {
        'get-all-congress-members-tweets': {
            'task': 'twitterapi.tasks.get_all_congress_members_tweets',
            'schedule': crontab(minute='*/10')
        }
}

@task()
def get_all_congress_members_tweets():
    congress_member_data = CongressMember.get_twitter_data()
    for member_id,twitter_screen_name in congress_member_data:
        if twitter_screen_name is not None:
            get_congress_member_tweets(member_id, twitter_screen_name)

@task()
def get_congress_member_tweets(member_id, twitter_screen_name):
    serializers = services.get_twitter_statuses(twitter_screen_name)
    for serializer in serializers:
        if serializer.is_valid():
            serializer.save(congress_member_id=member_id)



