import uuid
from django.db import models

class Legalities(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brawl = models.CharField(max_length=300)
    commander = models.CharField(max_length=300)
    duel = models.CharField(max_length=300)
    future = models.CharField(max_length=300)
    frontier = models.CharField(max_length=300)
    legacy = models.CharField(max_length=300)
    modern = models.CharField(max_length=300)
    pauper = models.CharField(max_length=300)
    penny = models.CharField(max_length=300)
    pioneer = models.CharField(max_length=300)
    standard = models.CharField(max_length=300)
    vintage = models.CharField(max_length=300)
