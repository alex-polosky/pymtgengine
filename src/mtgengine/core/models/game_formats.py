import uuid
from django.db import models

class GameFormats(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paper = models.BooleanField()
    mtgo = models.BooleanField()
    arena = models.BooleanField()
    shandalar = models.BooleanField()
    dreamcast = models.BooleanField()
