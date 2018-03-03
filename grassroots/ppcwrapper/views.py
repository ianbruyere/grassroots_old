from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import CongressMember, Bill, CongressMemberVotePosition
from . import serializers

class CongressMembersViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint for Individual Congress Members """
    queryset = CongressMember.objects.all()
    serializer_class = serializers.CongressMemberSerializer

class BillsViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Bill.objects.all()
     serializer_class = serializers.BillSerializer

class VotePositionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CongressMemberVotePosition.objects.all()
    serializer_class = serializers.CongressMemberVotePositionSerializer

