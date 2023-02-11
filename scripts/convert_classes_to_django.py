from abc import ABCMeta
import os
import typing
from mtgjson5.classes.mtgjson_card import MtgjsonCardObject
from mtgjson5.classes.mtgjson_deck_header import MtgjsonDeckHeaderObject
from mtgjson5.classes.mtgjson_deck import MtgjsonDeckObject
from mtgjson5.classes.mtgjson_foreign_data import MtgjsonForeignDataObject
from mtgjson5.classes.mtgjson_game_formats import MtgjsonGameFormatsObject
from mtgjson5.classes.mtgjson_identifiers import MtgjsonIdentifiersObject
from mtgjson5.classes.mtgjson_leadership_skills import MtgjsonLeadershipSkillsObject
from mtgjson5.classes.mtgjson_legalities import MtgjsonLegalitiesObject
from mtgjson5.classes.mtgjson_meta import MtgjsonMetaObject
# from mtgjson5.classes.mtgjson_prices import MtgjsonPricesObject
# from mtgjson5.classes.mtgjson_purchase_urls import MtgjsonPurchaseUrlsObject
# from mtgjson5.classes.mtgjson_related_cards import MtgjsonRelatedCardsObject
from mtgjson5.classes.mtgjson_rulings import MtgjsonRulingObject
from mtgjson5.classes.mtgjson_sealed_product import MtgjsonSealedProductObject
from mtgjson5.classes.mtgjson_set import MtgjsonSetObject
# from mtgjson5.classes.mtgjson_translations import MtgjsonTranslationsObject

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
OUT_DIR = os.path.join(BASE_DIR, 'src', 'mtgengine', 'core', 'models')

classes = (
    MtgjsonCardObject,
    MtgjsonDeckHeaderObject,
    MtgjsonDeckObject,
    MtgjsonForeignDataObject,
    MtgjsonGameFormatsObject,
    MtgjsonIdentifiersObject,
    MtgjsonLeadershipSkillsObject,
    MtgjsonLegalitiesObject,
    MtgjsonMetaObject,
    MtgjsonRulingObject,
    MtgjsonSealedProductObject,
    MtgjsonSetObject
)

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

def parse_name(clas: type):
    name = clas.__name__.replace('Mtgjson', '').replace('Object', '')
    if name == 'Meta':
        name = 'Meta_'
    if name == 'Set':
        name = 'Set_'
    return name

def gen_django_class(clas: type):
    name = parse_name(clas)
    imports = ['uuid', ('django.db', 'models')]
    fields = {
        'id': ['UUIDField', {
            'primary_key': 'True',
            'default': 'uuid.uuid4',
            'editable': 'False'
        }]
    }

    hints = typing.get_type_hints(clas)
    for field_name in hints:
        if field_name[0] == '_':
            continue

        type_ = hints[field_name]
        field_type = None
        field_args = {}
        
        if type(type_) != type:
            # parse out the type hint
            if type_.__name__ == 'Optional':
                type_ = typing.get_args(type_)[0]
                field_args['null'] = 'True'
                field_args['blank'] = 'True'
            if type_.__name__ == 'List':
                field_args['TODO_is_list'] = 'True'
                type_ = typing.get_args(type_)[0]
            if type_.__name__ == 'Dict':
                print(f'Not sure how to parse a dict yet, please check: {name}-{field_name}')
                continue
        if type(type_) not in (type, ABCMeta):
            print(f'Incorrectly parsed type: {name}-{field_name}')
            continue

        # check for built ins
        if type_ == str:
            if field_name == 'text':
                field_type = 'TextField'
            else:
                field_type = 'CharField'
                field_args['max_length'] = '300'
        elif type_ == float: # I can bet that this is actually a normal number
            field_type = 'FloatField'
        elif type_ == int:
            field_type = 'IntegerField'
        elif type_ == bool:
            field_type = 'BooleanField'
        else:
            # Assume class object
            if type_ not in classes:
                print(f'Attempted foreign key to unsupported class: {name}-{field_name}')
                continue

            field_type = 'ForeignKey'

            import_ = (f'mtgengine.core.models.{parse_key(parse_name(type_))}', parse_name(type_))
            if import_ not in imports:
                imports.append()

            field_args[0] = parse_name(type_)
            field_args['on_delete'] = 'models.CASCADE'

        fields[field_name] = [field_type, field_args]

    s = ''
    for import_ in imports:
        if isinstance(import_, tuple):
            im = f'from {import_[0]} import {import_[1]}'
        else:
            im = f'import {import_}'
        s += f'{im}\n'
    s += '\n'

    s += f'class {name}(models.Model):\n'
    s += '\n'
    for field_name in fields:
        field_def = fields[field_name]
        field_type = field_def[0]
        field_args: dict = field_def[1]
        target = field_args.get(0, None)
        if target:
            del field_args[0]
        s += f'    {field_name} = models.{field_type}({", ".join(([target] if target else []) + [f"{k}={field_args[k]}" for k in field_args])})\n'

    return parse_key(name), s

for clas in classes:
    name, s = gen_django_class(clas)
    with open(os.path.join(OUT_DIR, f'{name}.py'), 'w') as f:
        f.write(s)
