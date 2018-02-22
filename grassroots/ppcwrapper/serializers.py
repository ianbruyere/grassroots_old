import os
import requests
import json
from rest_framework import serializers
from datetime import datetime
from .models import CongressMember, Bill, Votes, CongressMemberVotePositions, Session
import logging


class CongressMemberSerializer(serializers.ModelSerializer):
    bills = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='bill-detail'
    )

    class Meta:
        model = CongressMember
        fields=('id', 'chamber' ,'first_name', 'last_name', 'state',
                'date_of_birth', 'in_office', 'party', 'twitter_account', 
                'facebook_account', 'youtube_account', 'govtrack_id',
                'cspan_id', 'votesmart_id', 'icpsr_id', 'crp_id', 'contact_form',
                'google_entity_id', 'api_uri', 'url', 'rss_url', 'bills'
                ) 
                
    def create(self, validated_data):
        return CongressMember.objects.create(**validated_data)
    
class BillSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Bill
        fields='__all__'

    def create(self, validated_data):
        return Bill.objects.create(**validated_data)

class CongressMemberVotePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CongressMemberVotePositions
        fields=('member_id','vote_position')

    def create(self, validated_data):
        return CongressMemberVotePositions.objects.create(**validated_data)


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Votes
        fields=('bill_id' ,'number', 'title', 'latest_action') 

    def create(self, validated_data):
        Votes.objects.create(**validated_data)

class SessionSerializer(serializers.ModelSerializer):
    bill = VotesSerializer(many=False, read_only=False)
    positions = CongressMemberVotePositionsSerializer(many=True)
    class Meta:
        model = Session
        fields = ('congress', 'chamber', 'session', 'roll_call',
        'source', 'url', 'vote_uri', 'question', 'description', 'vote_type',
         'date', 'time', 'result','bill','positions')

    def create(self, validated_data):
        bill_data = validated_data.pop('bill')
        positions_data = validated_data.pop('positions')
        session = Session.objects.create(**validated_data)
        votes = Votes.objects.create(session=session, **bill_data)
        for position in positions_data:
            CongressMemberVotePositions.objects.create(session=session, **position)
        return session