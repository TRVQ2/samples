import json
import csv

json_file_name = "market_types.json"
csv_file_name = "SC.csv"

with open(json_file_name, 'r') as f:
    json_list = json.loads(f.read())

with open(csv_file_name, 'r') as f:
    csv_list = list(csv.DictReader(f))

assert len(json_list) == len(csv_list), "Length is different"

for i in range(len(csv_list)):
    assert csv_list[i]["name"] == json_list[csv_list[i]["id"]], \
        f'i={i}, csv={csv_list[i]["name"]}, \
        json={json_list[csv_list[i]["id"]]}'
