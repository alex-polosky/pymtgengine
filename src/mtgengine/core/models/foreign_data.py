import uuid
from django.db import models

class ForeignData(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    language = models.CharField(max_length=300)
    multiverse_id = models.IntegerField(null=True, blank=True)
    face_name = models.CharField(null=True, blank=True, max_length=300)
    flavor_text = models.CharField(null=True, blank=True, max_length=300)
    name = models.CharField(null=True, blank=True, max_length=300)
    text = models.TextField(null=True, blank=True)
    type = models.CharField(null=True, blank=True, max_length=300)
