import json

market_types_file_name = "market_types.json"
parameters = json.loads(open(market_types_file_name, 'r').read())

output = []
for i in parameters:
    market_type = {
        "entity": {
            "id": "14_" + i,
            "marketTypeId": i,
            "marketTypeName": "[SC] " + parameters[i],
            "selectionNameTemplate": "",
            "sportId": "14",
            "playType": "PRE_PLAY",
            "betBuilder": True
        },
        "translations": [{
            "entityId": "14_" + i,
            "parentOrder": 0,
            "order": 0,
            "entityType": "MARKET_TYPE",
            "fieldName": "selectionNameTemplate",
            "value": "",
            "lang": "original"
        }]
    }
    output.append(market_type)

json_dump = json.dumps(output, indent=2)
open("out_" + market_types_file_name, 'w').write(json_dump)
