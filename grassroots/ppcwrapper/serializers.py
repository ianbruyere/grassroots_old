from .models import SenateMember
from rest_framework import serializers
from . import services
import os
import requests
import json
from datetime import datetime

class SenateMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = SenateMember
        fields=('id', 'first_name', 'last_name', 'state',
                'date_of_birth', 'in_office', 'twitter_account', 
                'facebook_account', 'youtube_account', 'govtrack_id',
                'cspan_id', 'votesmart_id', 'icpsr_id', 'crp_id',
                'google_entity_id', 'api_uri', 'url', 'rss_url', 'contact_form'
                )

    def create(self, validated_data):
        return SenateMember.objects.create(**validated_data)
        
    def get_data():
        return services.get_senate_members()

#TODO: Make other ModelSerializers

