from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class PodcastModel(models.Model):
    title = models.CharField(max_length = 500, null = True)
    description =  models.CharField(max_length = 20, null = True)
    photo_url = models.CharField(max_length = 30, null = True)
    category = models.JSONField()
    

class EpisodeModel(PodcastModel):
    summary = models.CharField(max_length = 1000, null = True)



    