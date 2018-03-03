from celery import task
from celery.schedules import crontab
from grassroots.celery import app
from . import services
from .models import CongressMember, Bill, CongressMemberVotePosition
from .serializers import CongressMemberSerializer, BillSerializer, CongressMemberVotePositionSerializer
import logging

app.conf.beat_schedule = {
        'get-congress-members': {
            'task': 'ppcwrapper.tasks.get_congress_members',
            'schedule': crontab(minute='*/1')
        },
        'get-recent-senate-bills': {
            'task': 'ppcwrapper.tasks.get_recent_senate_bills',
            'schedule': crontab(minute='*/1')
        }
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
def get_congress_member_vote_positions(member_id):
    client = services.CongressMembersClient()
    votePositionsData = client.get_vote_positions(member_id)
    currentPositionData =  CongressMemberVotePosition.objects.filter(member_id=member_id)
    for i in votePositionsData['results'][0]['votes']:
        bill = get_or_create_bill(i['bill'])
        if bill == None:
            continue
        if  not currentPositionData.filter(bill_id=bill).exists():
            serializer = CongressMemberVotePositionSerializer(data=i)
            if serializer.is_valid():
                serializer.save(bill_id=bill)


# Helper Functions
def create_or_update(newData, currentData, serializerType, chamber, idName='id'): # TODO:change chamber to be a tuple of arguments
    for i in newData:
        serializer = serializerType
        if currentData.filter(pk=i[idName]).exists():
            serializer = serializerType(currentData.get(pk=i[idName]), data=i)
        else:
            serializer = serializerType(data=i)
        if serializer.is_valid():
            serializer.save(chamber=chamber)

def get_or_create_bill(billData):
    if not Bill.objects.filter(pk=billData['bill_id']).exists():
        client = services.BillClient()
        key = determine_bill_key(billData)
        if billData[key] == None:
            return None
        newBillData = client.raw_requester(billData[key]) 
        serializer = BillSerializer(data=newBillData['results'][0])
        if serializer.is_valid():
            serializer.save()
        else:
            logging.warning(serializer.errors)
            return None
    return Bill.objects.get(pk=billData['bill_id'])
    
def determine_bill_key(billData):
    key = 'api_uri' if 'api_uri' in billData else 'bill_uri'
    return key

