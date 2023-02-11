import uuid
from django.db import models

class Identifiers(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_kingdom_etched_id = models.CharField(null=True, blank=True, max_length=300)
    card_kingdom_foil_id = models.CharField(null=True, blank=True, max_length=300)
    card_kingdom_id = models.CharField(null=True, blank=True, max_length=300)
    cardsphere_id = models.CharField(null=True, blank=True, max_length=300)
    mcm_id = models.CharField(null=True, blank=True, max_length=300)
    mcm_meta_id = models.CharField(null=True, blank=True, max_length=300)
    mtg_arena_id = models.CharField(null=True, blank=True, max_length=300)
    mtgjson_foil_version_id = models.CharField(null=True, blank=True, max_length=300)
    mtgjson_non_foil_version_id = models.CharField(null=True, blank=True, max_length=300)
    mtgjson_v4_id = models.CharField(null=True, blank=True, max_length=300)
    mtgo_foil_id = models.CharField(null=True, blank=True, max_length=300)
    mtgo_id = models.CharField(null=True, blank=True, max_length=300)
    multiverse_id = models.CharField(null=True, blank=True, max_length=300)
    scryfall_id = models.CharField(null=True, blank=True, max_length=300)
    scryfall_illustration_id = models.CharField(null=True, blank=True, max_length=300)
    scryfall_oracle_id = models.CharField(null=True, blank=True, max_length=300)
    tcgplayer_etched_product_id = models.CharField(null=True, blank=True, max_length=300)
    tcgplayer_product_id = models.CharField(null=True, blank=True, max_length=300)
