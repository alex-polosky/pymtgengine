import uuid
from django.db import models
from mtgengine.core.models.card import Card
from mtgengine.core.models.sealed_product import SealedProduct
from mtgengine.core.models.card import Card

class Set_(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    base_set_size = models.IntegerField()
    block = models.CharField(max_length=300)
    cards = models.ForeignKey(Card, TODO_is_list=True, on_delete=models.CASCADE)
    cardsphere_set_id = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=300)
    code_v3 = models.CharField(max_length=300)
    is_foreign_only = models.BooleanField()
    is_foil_only = models.BooleanField()
    is_non_foil_only = models.BooleanField()
    is_online_only = models.BooleanField()
    is_partial_preview = models.BooleanField()
    keyrune_code = models.CharField(max_length=300)
    languages = models.CharField(TODO_is_list=True, max_length=300)
    mcm_id = models.IntegerField(null=True, blank=True)
    mcm_id_extras = models.IntegerField(null=True, blank=True)
    mcm_name = models.CharField(null=True, blank=True, max_length=300)
    mtgo_code = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    parent_code = models.CharField(max_length=300)
    release_date = models.CharField(max_length=300)
    tcgplayer_group_id = models.IntegerField(null=True, blank=True)
    sealed_product = models.ForeignKey(SealedProduct, TODO_is_list=True, on_delete=models.CASCADE)
    tokens = models.ForeignKey(Card, TODO_is_list=True, on_delete=models.CASCADE)
    token_set_code = models.CharField(null=True, blank=True, max_length=300)
    total_set_size = models.IntegerField()
    type = models.CharField(max_length=300)
    search_uri = models.CharField(max_length=300)
