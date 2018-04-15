from django.db import models
import datetime

class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    congress_member_id = models.CharField(max_length=300)
    text = models.TextField()
    created_at = models.CharField(max_length=300)