import json
from pprint import pprint
from mtgjson5.classes.mtgjson_card import MtgjsonCardObject

unique_keys = ['artist',
 'asciiName',
 'attractionLights',
 'availability',
 'boosterTypes',
 'borderColor',
 'cardParts',
 'colorIdentity',
 'colorIndicator',
 'colors',
 'convertedManaCost',
 'duelDeck',
 'edhrecRank',
 'edhrecSaltiness',
 'faceConvertedManaCost',
 'faceFlavorName',
 'faceManaValue',
 'faceName',
 'finishes',
 'firstPrinting',
 'flavorName',
 'flavorText',
 'foreignData',
 'frameEffects',
 'frameVersion',
 'hand',
 'hasAlternativeDeckLimit',
 'hasContentWarning',
 'hasFoil',
 'hasNonFoil',
 'identifiers',
 'isAlternative',
 'isFullArt',
 'isFunny',
 'isOnlineOnly',
 'isOversized',
 'isPromo',
 'isRebalanced',
 'isReprint',
 'isReserved',
 'isStarter',
 'isStorySpotlight',
 'isTextless',
 'isTimeshifted',
 'keywords',
 'language',
 'layout',
 'leadershipSkills',
 'legalities',
 'life',
 'loyalty',
 'manaCost',
 'manaValue',
 'name',
 'number',
 'originalPrintings',
 'originalReleaseDate',
 'originalText',
 'originalType',
 'otherFaceIds',
 'power',
 'printings',
 'promoTypes',
 'purchaseUrls',
 'rarity',
 'rebalancedPrintings',
 'relatedCards',
 'rulings',
 'securityStamp',
 'setCode',
 'side',
 'signature',
 'subset',
 'subtypes',
 'supertypes',
 'text',
 'toughness',
 'type',
 'types',
 'uuid',
 'variations',
 'watermark']

card = MtgjsonCardObject()

a = 20
