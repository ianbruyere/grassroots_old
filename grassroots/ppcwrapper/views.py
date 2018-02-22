from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import CongressMember, Bill, CongressMemberVotePositions, Session
from .serializers import CongressMemberSerializer, BillSerializer, VotesSerializer, SessionSerializer
from .tasks import get_specfic_roll_call
from . import services


class CongressMembersViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint for Individual Congress Members """
    queryset = CongressMember.objects.all()
    serializer_class = CongressMemberSerializer

class RecentBillsViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Bill.objects.all()
     serializer_class = BillSerializer

class SpecificVoteSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    #TODO I need to start up here again and also figure out the get/update for 
    # the specfic roll call, right now vote is using a weird unique_together
    # which I can see as being a problem in the future
    # so possibly going off the bill_id will be the way to go, I think I would be able to select 
    # it we will see
    # currentVoteData = VotesPerBill.objects.all()

    # client = services.VoteClient()
    # rollCallData = client.get_specific_roll_call('senate', '2')
    # serializer = VotesSerializer(data=rollCallData['results']['votes']['vote'])
    # if serializer.is_valid():
    #     serializer.save(chamber='senate')
    # queryset = CongressMemberVotePositions.objects.all()
    # serializer_class = VotesSerializer

#TODO: Hookup other views for other API calles within PPC

