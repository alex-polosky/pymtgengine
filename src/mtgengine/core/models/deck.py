import uuid
from django.db import models

class Deck(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    release_date = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    file_name = models.CharField(max_length=300)
