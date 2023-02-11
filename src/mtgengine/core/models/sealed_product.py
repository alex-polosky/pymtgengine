import uuid
from django.db import models
from mtgengine.core.models.identifiers import Identifiers

class SealedProduct(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    uuid = models.CharField(max_length=300)
    identifiers = models.ForeignKey(Identifiers, on_delete=models.CASCADE)
    release_date = models.CharField(null=True, blank=True, max_length=300)
    product_size = models.IntegerField(null=True, blank=True)
