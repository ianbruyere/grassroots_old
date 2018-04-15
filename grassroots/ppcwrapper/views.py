from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, generics
from .models import CongressMember, Bill, CongressMemberVotePosition
from . import serializers

#TODO Need to pickle this so that I can cache the responses. 
# Note: need to actualy look into pickling and cacheing
class CongressMembersViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint for Individual Congress Members """
    serializer_class = serializers.CongressMemberSerializer

    def get_queryset(self):
        queryset = CongressMember.objects.all()
        member_id = self.request.query_params.get('member_id')
        if member_id is not None:
            queryset = queryset.filter(id=member_id)
        return queryset

class BillsViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Bill.objects.all()
     serializer_class = serializers.BillSerializer

class VotePositionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CongressMemberVotePosition.objects.all()
    serializer_class = serializers.CongressMemberVotePositionSerializer

