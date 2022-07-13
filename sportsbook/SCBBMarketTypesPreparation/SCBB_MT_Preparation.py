import csv
import json

csv_file_name = "SC.csv"
with open(csv_file_name, 'r') as f:
    csv_list = list(csv.DictReader(f))

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
with open("out.json", 'w') as f:
    f.write(json_dump)
