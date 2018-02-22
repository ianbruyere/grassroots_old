from celery import task
from celery.schedules import crontab
from grassroots.celery import app
from . import services
from .models import CongressMember, Bill, Session
from .serializers import CongressMemberSerializer, BillSerializer, VotesSerializer
import logging

app.conf.beat_schedule = {
        'get-congress-members': {
            'task': 'ppcwrapper.tasks.get_congress_members',
            'schedule': crontab(minute='*/1')
        },
        'get-recent-senate-bills': {
            'task': 'ppcwrapper.tasks.get_recent_senate_bills',
            'schedule': crontab(minute='*/1')
        },
        # 'get-specific-roll-call' : {
        #     'task' : 'ppcwrapper.tasks.get_specific_roll_call',
        #     'schedule': crontab(minute='*/1')
        # }
}

@task()
def get_congress_members():
    client = services.CongressMembersClient()
    senateData = client.get_members('senate')
    houseData = client.get_members('house')

    currentCongressMemberData = CongressMember.objects.all()
    create_or_update(senateData['results'][0]['members'], currentCongressMemberData, CongressMemberSerializer, 'senate', 'id')
    create_or_update(houseData['results'][0]['members'], currentCongressMemberData, CongressMemberSerializer,'house', 'id')

@task()
def get_recent_senate_bills():
    client = services.BillClient()
    billData = client.get_recent_bills('senate', 'introduced')

    currentBillData = Bill.objects.all()
    create_or_update(billData['results'][0]['bills'], currentBillData, BillSerializer, 'senate', 'bill_id')

@task()
def get_specfic_roll_call():
    client = services.VoteClient()
    rollCallData = client.get_specific_roll_call('senate', '2')

    #TODO I need to start up here again and also figure out the get/update for 
    # the specfic roll call, right now vote is using a weird unique_together
    # which I can see as being a problem in the future
    # so possibly going off the bill_id will be the way to go, I think I would be able to select 
    # it we will see
    # currentVoteData = VotesPerBill.objects.all()
    for i in rollCallData['results']['votes']:
        serializer = VotesSerializer(data=i) 
        if serializer.is_valid():
            serializer.save(chamber='senate')

# Helper Functions
def create_or_update(newData, currentData, serializerType, chamber, idName): # TODO:change chamber to be a tuple of arguments
    for i in newData:
        serializer = serializerType
        if currentData.filter(pk=i[idName]).exists():
            serializer = serializerType(currentData.get(pk=i[idName]), data=i)
        else:
            serializer = serializerType(data=i)
        if serializer.is_valid():
            serializer.save(chamber=chamber)