from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import SenateMember
from .serializers import SenateMemberSerializer
from . import services

class SenateMembersViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint for Individual Senate Members """
    # TODO: Will be migrated as a scheduled task in celery
    raw_data = SenateMemberSerializer.get_data()
    for i in raw_data['results'][0]['members']:
        serializer = SenateMemberSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
        
        
    queryset = SenateMember.objects.all()
    serializer_class = SenateMemberSerializer

#TODO: Hookup other views for other API calles within PPC
