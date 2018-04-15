from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, generics
from .models import Status
from . import serializers

class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    """API Endpoint for Congress Member Tweet Statuses"""
    serializer_class = serializers.StatusSerializer

    def get_queryset(self):
        queryset = Status.objects.all()
        member_id = self.request.query_params.get('member_id')
        if member_id is not None:
            queryset = queryset.filter(congress_member_id=member_id)
        return queryset