from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import CongressMember
from .serializers import CongressMemberSerializer


class CongressMembersViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint for Individual Congress Members """
    queryset = CongressMember.objects.all()
    serializer_class = CongressMemberSerializer

#TODO: Hookup other views for other API calles within PPC

