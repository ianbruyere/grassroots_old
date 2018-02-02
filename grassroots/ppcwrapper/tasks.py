from celery import task
from celery.schedules import crontab
from grassroots.celery import app
from . import services
from .models import CongressMember
from .serializers import CongressMemberSerializer

app.conf.beat_schedule = {
        'get-congress-members': {
        'task': 'ppcwrapper.tasks.get_congress_members',
        'schedule': crontab(minute='*/1')
        }
}

@task()
def get_congress_members():
    senateData = services.CongressMembersClient.get_members('senate')
    houseData = services.CongressMembersClient.get_members('house')

    currentCongressMemberData = CongressMember.objects.all()
    get_or_update(senateData['results'][0]['members'], currentCongressMemberData, CongressMemberSerializer, "senate")
    get_or_update(houseData['results'][0]['members'], currentCongressMemberData, CongressMemberSerializer, "house")


# Helper Functions
def get_or_update(newData, currentData, serializerType, chamber): # TODO:change chamber to be a tuple of arguments
    for i in newData:
        serializer = serializerType
        if currentData.filter(id=i["id"]).exists():
            serializer = serializerType(currentData.get(id=i['id']), data=i)
        else:
            serializer = serializerType(data=i)
        if serializer.is_valid():
            serializer.save(chamber=chamber)
