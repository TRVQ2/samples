import csv
import json

csv_file_name = "SC.csv"
csv_list = list(csv.DictReader(open(csv_file_name)))

output = []
for i in csv_list:
    market_type = {
        "entity": {
            "id": "14_" + i["id"],
            "marketTypeId": i["id"],
            "marketTypeName": "[SC] " + i["name"],
            "selectionNameTemplate": None,
            "sportId": "14",
            "playType": "PRE_PLAY",
            "betBuilder": True,
            "attributes": []
        },
        "translations": []
    }
    if i["periodType"] != '':
        market_type["entity"]["attributes"].append(
            {"type": "periodType", "value": i["periodType"]}
        )
    if i["kind"] != '':
        market_type["entity"]["attributes"].append(
            {"type": "marketKind", "value": i["kind"]}
        )

    output.append(market_type)

json_dump = json.dumps(output, indent=2)
open("out.json", 'w').write(json_dump)
