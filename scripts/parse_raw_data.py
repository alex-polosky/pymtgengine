import json
import os
from pprint import pprint
import typing
from mtgjson5.classes.mtgjson_card import MtgjsonCardObject
from mtgjson5.classes.mtgjson_game_formats import  MtgjsonGameFormatsObject
from mtgjson5.classes.mtgjson_identifiers import MtgjsonIdentifiersObject
from mtgjson5.classes.mtgjson_leadership_skills import MtgjsonLeadershipSkillsObject
from mtgjson5.classes.mtgjson_legalities import MtgjsonLegalitiesObject
# from mtgjson5.classes.mtgjson_prices import MtgjsonPricesObject
from mtgjson5.classes.mtgjson_purchase_urls import MtgjsonPurchaseUrlsObject
from mtgjson5.classes.mtgjson_rulings import MtgjsonRulingObject


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
OUT_DIR = os.path.join(BASE_DIR, 'data', 'cards')

with open(os.path.join(DATA_DIR, 'AtomicCards.json')) as f:
    cards_atomic_raw = json.loads(f.read())['data']

with open(os.path.join(DATA_DIR, 'AllPrintings.json')) as f:
    cards_by_set_raw = json.loads(f.read())['data']


def parse_key(s):
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''
    for i in range(len(s)):
        c = s[i]
        if c in caps:
            c = c.lower()
            if len(key) > 0:
                c = '_' + c
        key += c
    return key

def parse_simple_obj(obj: dict, clas: type):
    type_hints = typing.get_type_hints(clas.__init__)
    args = [None for i in range(len(type_hints) - 1)]
    instance = clas(*args)
    for key in obj:
        setattr(instance, key, obj[key])
    return instance

def parse_card(obj: dict):
    is_token = obj.get('layout') == 'token'
    card = MtgjsonCardObject(is_token)
    type_hints = typing.get_type_hints(card)
    for o_key in obj:
        c_key = parse_key(o_key)
        value = obj[o_key]
        if c_key not in type_hints:
            print(f'card missing attr: {c_key}')
            continue
        if o_key == 'availability':
            n =  MtgjsonGameFormatsObject()
            for format_ in value:
                setattr(n, format_, True)
            value = n; del n
        if o_key == 'foreignData':
            # I'm an asshole and don't currently want to implement i18n, sorry
            continue
        if o_key == 'identifiers':
            value = parse_simple_obj(value, MtgjsonIdentifiersObject)
        if o_key == 'leadershipSkills':
            value = parse_simple_obj(value, MtgjsonLeadershipSkillsObject)
        if o_key == 'legalities':
            value = parse_simple_obj(value, MtgjsonLegalitiesObject)
        if o_key == 'purchaseUrls':
            value = parse_simple_obj(value, MtgjsonPurchaseUrlsObject)
        if o_key == 'relatedCards':
            print(f'[{obj.get("name")}] relatedCards.active')
        if o_key == 'rulings':
            n = []
            for ruling_ in value:
                n.append(parse_simple_obj(ruling_, MtgjsonRulingObject))
            value = n; del n
        
        if o_key in ('hasFoil', 'hasNonFoil', ):
            # deprecated keys
            continue
            
        setattr(card, c_key, value)
    return card

cards_atomic = []
for cards_ in cards_atomic_raw.values():
    for card_ in cards_:
        card = parse_card(card_)
        cards_atomic.append(card)

cards_by_set = {}
for set_ in cards_by_set_raw:
    cards_by_set[set_] = []
    for card_ in cards_by_set_raw[set_]['cards']:
        card = parse_card(card_)
        cards_by_set[set_].append(card)

del cards_atomic_raw, cards_by_set_raw


import pickle
with open(os.path.join(OUT_DIR, 'atomic.pickle'), 'wb') as f:
    f.write(pickle.dumps(cards_atomic))
with open(os.path.join(OUT_DIR, 'by_set.pickle'), 'wb') as f:
    f.write(pickle.dumps(cards_by_set))

a = 20
