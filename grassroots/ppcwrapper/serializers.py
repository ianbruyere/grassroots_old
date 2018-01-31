import os
import requests
import json
from rest_framework import serializers
from datetime import datetime
from .models import CongressMember


class CongressMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = CongressMember
        fields=('id', 'chamber' ,'first_name', 'last_name', 'state',
                'date_of_birth', 'in_office', 'party', 'twitter_account', 
                'facebook_account', 'youtube_account', 'govtrack_id',
                'cspan_id', 'votesmart_id', 'icpsr_id', 'crp_id',
                'google_entity_id', 'api_uri', 'url', 'rss_url', 
                'contact_form'
                )

    def create(self, validated_data):
        return CongressMember.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.chamber = validated_data.get('chamber', instance.chamber)
    #     instance.save()
    #     return instance


    
        

#TODO: Make other ModelSerializers

