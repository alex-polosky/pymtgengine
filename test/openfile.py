import json
from mtgjson5.classes.mtgjson_card import MtgjsonCardObject

with open('AtomicCards.json') as f:
    data_atomic = json.loads(f.read())

print(data_atomic['data'][list(data_atomic['data'].keys())[-100]])

# -> {
#     "meta": {},
#     "data": {
#         "[card_name]": {}
#     }
# }

with open('AllPrintings.json') as f:
    data_all = json.loads(f.read())

# -> {
#     "meta": {},
#     "data": {
#         "[set_code]": {
#             "baseSetSize": 1,
#             "booster": {
#                 "arena": ?,
#                 "default": ?
#             },
#             "cards": [],
#             "code": "[set_code]",
#             "isFoilOnly": true,
#             "isOnlineOnly": true,
#             "keyruneCode": "",
#             "languages": [],
#             "mcmId": 1,
#             "mcmIdExtras": 1,
#             "mcmName": "",
#             "mtgoCode": "",
#             "name": "",
#             "releaseDate": "",
#             "sealedProduct": [],
#             "tcgplayerGroupId": 1,
#             "tokenSetCode": "",
#             "tokens": [],
#             "totalSetSize": 1,
#             "translations": {},
#             "type": ""
#         }
#     }
# }

print(data_all['data']['ONE']['cards'][0])
