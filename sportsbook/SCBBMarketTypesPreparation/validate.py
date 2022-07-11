import json
import csv

json_file_name = "market_types.json"
csv_file_name = "SC.csv"
json_list = json.loads(open(json_file_name, 'r').read())
csv_list = list(csv.DictReader(open(csv_file_name)))

assert len(json_list) == len(csv_list), "Length is different"

for i in range(len(csv_list)):
    assert csv_list[i]["name"] == json_list[csv_list[i]["id"]], \
        f'i={i}, csv={csv_list[i]["name"]}, \
        json={json_list[csv_list[i]["id"]]}'
