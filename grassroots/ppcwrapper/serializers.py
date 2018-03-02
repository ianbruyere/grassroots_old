from .models import SenateMember
from rest_framework import serializers
from . import services
import os
import requests
import json
from datetime import datetime
<<<<<<< Updated upstream
=======
from .models import CongressMember, Bill, Votes, CongressMemberVotePosition
import logging
>>>>>>> Stashed changes

class SenateMemberSerializer(serializers.ModelSerializer):

    # positions = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='congressmembervoteposition-detail'
    # )

    class Meta:
        model = SenateMember
        fields=('id', 'first_name', 'last_name', 'state',
                'date_of_birth', 'in_office', 'party', 'twitter_account', 
                'facebook_account', 'youtube_account', 'govtrack_id',
<<<<<<< Updated upstream
                'cspan_id', 'votesmart_id', 'icpsr_id', 'crp_id',
                'google_entity_id', 'api_uri', 'url', 'rss_url', 'contact_form'
                )
=======
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

class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Votes
        fields=('bill_id' ,'number', 'title', 'latest_action') 
>>>>>>> Stashed changes

    def create(self, validated_data):
        return SenateMember.objects.create(**validated_data)
        
    def get_data():
        return services.get_senate_members()

<<<<<<< Updated upstream
#TODO: Make other ModelSerializers

=======
class CongressMemberVotePositionSerializer(serializers.ModelSerializer):
    # bill = VotesSerializer()

    class Meta:
        model = CongressMemberVotePosition
        fields=('member_id', 'chamber', 'session', 'roll_call',
        'vote_uri', 'description', 'question', 'result',
        'date', 'time', 'position')

    def create(self, validated_data):
        # bill_data = validated_data.pop('bill')
        # vote = Votes.object.create(**bill_data)
        return CongressMemberVotePosition.objects.create(**validated_data)
# class SessionSerializer(serializers.ModelSerializer):
#     bill = VotesSerializer(many=False, read_only=False)
#     positions = CongressMemberVotePositionsSerializer(many=True)
#     class Meta:
#         model = Session
#         fields = ('congress', 'chamber', 'session', 'roll_call',
#         'source', 'url', 'vote_uri', 'question', 'description', 'vote_type',
#          'date', 'time', 'result','bill','positions')

#     def create(self, validated_data):
#         bill_data = validated_data.pop('bill')
#         positions_data = validated_data.pop('positions')
#         session = Session.objects.create(**validated_data)
#         votes = Votes.objects.create(session=session, **bill_data)
#         for position in positions_data:
#             CongressMemberVotePositions.objects.create(session=session, **position)
#         return sessionr a

>>>>>>> Stashed changes
