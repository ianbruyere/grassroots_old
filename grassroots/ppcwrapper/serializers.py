from .models import CongressMember, Bill, CongressMemberVotePosition
from rest_framework import serializers
import os
import requests
import json
from rest_framework import serializers
from datetime import datetime
import logging


class CongressMemberSerializer(serializers.ModelSerializer):
    sponsoredbills = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='bill-detail'
    )
    votes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='congressmembervoteposition-detail'
    )

    class Meta:
        model = CongressMember
        fields=('id', 'first_name', 'last_name', 'state',
                'date_of_birth', 'in_office', 'party', 'twitter_account', 
                'facebook_account', 'youtube_account', 'govtrack_id',
                'cspan_id', 'votesmart_id', 'icpsr_id', 'crp_id', 
                'contact_form', 'google_entity_id', 'api_uri', 
                'url', 'rss_url', 'sponsoredbills', 'votes'
                ) 
                
    def create(self, validated_data):
        return CongressMember.objects.create(**validated_data)
    
class CongressMemberVotePositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CongressMemberVotePosition
        fields=('member_id', 'chamber', 'session', 'roll_call',
        'vote_uri', 'description', 'question', 'result',
        'date', 'time', 'position')

    def create(self, validated_data):
        return CongressMemberVotePosition.objects.create(**validated_data)
        
class BillSerializer(serializers.ModelSerializer): 
    votepositions = CongressMemberVotePositionSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Bill
        fields=('bill_id', 'congress', 'bill_type', 'number', 'bill_uri', 
        'title', 'short_title', 'cosponsored_date', 'introduced_date',
        'sponsor_title', 'sponsor_id', 'sponsor_name', 'sponsor_state',
        'sponsor_party', 'sponsor_uri', 'gpo_pdf_uri', 'congressdotgov_url',
        'govtrack_url', 'active', 'last_vote', 'house_passage', 'senate_passage',
        'enacted', 'vetoed', 'cosponsors', 'committees', 'primary_subject',
        'summary', 'latest_major_action_date', 'latest_major_action',
        'chamber', 'votepositions')

    def create(self, validated_data):
        return Bill.objects.create(**validated_data)
