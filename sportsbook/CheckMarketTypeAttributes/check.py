import json

file_name = "exportMarketTypes.json"
parameters = json.loads(open(file_name, 'r').read())

for item in parameters:
    # correct 'selectionNameTemplate' and 'translations'
    if 'selectionNameTemplate' not in item['entity']:
        item['entity']['selectionNameTemplate'] = None
        item['translations'] = []
    else:
        selectionNameTemplate = item['entity']['selectionNameTemplate']
        if selectionNameTemplate is None or selectionNameTemplate == '':
            item['entity']['selectionNameTemplate'] = None
            item['translations'] = []
        elif 'translations' not in item or item['translations'] is None:
            item['translations'] = [{
                "entityId": item['entity']['id'],
                "fieldName": "selectionNameTemplate",
                "entityType": "MARKET_TYPE",
                "lang": "original",
                "value": selectionNameTemplate,
                "order": 0,
                "parentOrder": 0
            }]
        else:
            # clean up originals
            for i in item['translations'][::-1]:
                if i['lang'] == 'original':
                    item['translations'].remove(i)

            item['translations'].append({
                "entityId": item['entity']['id'],
                "fieldName": "selectionNameTemplate",
                "entityType": "MARKET_TYPE",
                "lang": "original",
                "value": selectionNameTemplate,
                "order": 0,
                "parentOrder": 0
            })
    # remove Bet Builder attributes
    if 'attributes' in item['entity']:
        attributes = item['entity']['attributes']
        if (attributes is not None and len(attributes) > 0):
            for i in attributes[::-1]:
                if i['type'] in ('participantType', 'team'):
                    attributes.remove(i)
                elif i['type'] == 'periodType':
                    if i['value'] not in ("10MIN", "FH", "SH", "FT"):
                        attributes.remove(i)

json_dump = json.dumps(parameters, indent=2)
open("out_" + file_name, 'w').write(json_dump)
