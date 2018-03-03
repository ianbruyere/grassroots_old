# from django.contrib.postgres.fields import JSONField
from django.db import models
import datetime

# Create your models here.
class CongressMember(models.Model):
    id = models.CharField(primary_key=True, max_length=300)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    # Personal Info
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    date_of_birth = models.CharField(max_length=300, null=True)
    
    # Political Office Items
    in_office = models.NullBooleanField()
    party = models.CharField(max_length=300, null=True)
    
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

class Bill(models.Model):
    bill_id = models.CharField(primary_key=True, max_length=300)
    congress = models.CharField(max_length=300, null=True)
    bill_type = models.CharField(max_length=300, null=True)
    number = models.CharField(max_length=300, null=True)
    bill_uri = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=300, null=True)
    short_title = models.CharField(max_length=300, null=True)
    cosponsored_date = models.CharField(max_length=300, null=True)
    introduced_date= models.CharField(max_length=300, null=True)
    sponsor_title = models.CharField(max_length=300, null=True)
    sponsor_id = models.ForeignKey(CongressMember, related_name='sponsoredbills', on_delete=models.CASCADE)
    sponsor_name = models.CharField(max_length=300, null=True)
    sponsor_state = models.CharField(max_length=300, null=True)
    sponsor_party = models.CharField(max_length=300, null=True)
    sponsor_uri = models.URLField(blank=True, null=True)
    gpo_pdf_uri = models.URLField(blank=True, null=True)
    congressdotgov_url = models.URLField(null=True, blank=True)
    govtrack_url = models.URLField(null=True, blank=True)
    active = models.NullBooleanField()
    last_vote = models.CharField(max_length=300, blank=True, null=True)
    house_passage = models.CharField(max_length=300, blank=True, null=True)
    senate_passage = models.CharField(max_length=300, blank=True, null=True)
    enacted = models.CharField(max_length=300, blank=True, null=True)
    vetoed = models.CharField(max_length=300, blank=True, null=True)
    cosponsors = models.IntegerField(blank=True, null=True)
    committees = models.CharField(max_length=300, blank=True)
    primary_subject = models.CharField(max_length=300, blank=True)
    summary = models.TextField(blank=True) #TODO
    latest_major_action_date = models.CharField(max_length=300, blank=True)
    latest_major_action = models.TextField(blank=True) #TODO
    chamber = models.CharField(max_length=300, null=True)

    def get_primary_subjects():
        Bill.objects.all().values_list('primary_subject', flat=True)


class Votes(models.Model):
    number = models.CharField(max_length=300)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    bill_uri = models.CharField(max_length=300, blank=True)
    title = models.TextField()
    latest_action = models.TextField()
    
class CongressMemberVotePosition(models.Model):
    class Meta:
        unique_together = ('member_id', 'bill_id')

    member_id = models.ForeignKey(CongressMember, related_name='votes', on_delete=models.CASCADE)
    chamber = models.CharField(max_length=300)
    session = models.CharField(max_length=300)
    roll_call = models.CharField(max_length=300)
    vote_uri = models.CharField(max_length=300)
    bill_id = models.ForeignKey(Bill, related_name='votepositions', on_delete=models.CASCADE)
    description = models.TextField()
    question = models.CharField(max_length=300)
    result = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    position = models.CharField(max_length=300)