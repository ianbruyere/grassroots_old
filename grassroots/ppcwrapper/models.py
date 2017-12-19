# from django.contrib.postgres.fields import JSONField
from django.db import models
import datetime

# Create your models here.
class SenateMember(models.Model):
    id = models.CharField(primary_key=True, max_length=300)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    # Personal Info
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    date_of_birth = models.CharField(max_length=300, null=True)
    
    # Political Office Items
    in_office = models.NullBooleanField()
    
    # Social Media
    twitter_account = models.CharField(max_length=300, null=True, blank=True)
    facebook_account = models.CharField(max_length=300, null=True, blank=True)
    youtube_account = models.CharField(max_length=300, null=True, blank=True)

    # Various ids to to utilize 
    govtrack_id = models.IntegerField(null=True, blank=True)
    cspan_id = models.IntegerField(null=True, blank=True)
    votesmart_id = models.IntegerField(null=True, blank=True)
    icpsr_id = models.IntegerField(null=True, blank=True)
    crp_id = models.CharField(max_length=300, null=True, blank=True)
    google_entity_id = models.CharField(max_length=300, null=True, blank=True)

    # Various urls 
    api_uri = models.URLField(null=True, blank=True) #
    url = models.URLField(null=True, blank=True) # personal website
    rss_url = models.URLField(null=True, blank=True)
    contact_form = models.URLField(null=True, blank=True) 

#TODO: Need to make other models for endpoints