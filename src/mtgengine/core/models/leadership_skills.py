import uuid
from django.db import models

class LeadershipSkills(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brawl = models.BooleanField()
    commander = models.BooleanField()
    oathbreaker = models.BooleanField()
