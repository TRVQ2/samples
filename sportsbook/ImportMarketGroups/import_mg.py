import json

is_it_for_nl = True
file_name = "exportAllMarketGroups.json"
parameters = json.loads(open(file_name, 'r').read())


def build_name_translation(entityId, value):
    return {
        "entityId": entityId,
        "parentOrder": 0,
        "order": 0,
        "entityType": "MARKET_GROUP",
        "fieldName": "name",
        "value": value,
        "lang": "original"
    }


def build_badge_translation(entityId, value, lang="original"):
    return {
        "entityId": entityId,
        "parentOrder": 0,
        "order": 0,
        "entityType": "MARKET_GROUP_BADGE",
        "fieldName": "text",
        "value": value,
        "lang": lang
    }


for item in parameters:
    if item['entity']['badge'] is None:
        item['entity']['badge'] = {"text": ""}
    elif item['entity']['badge']['text'] is None:
        item['entity']['badge']['text'] = ''

    if item['translations'] is None:
        entity_id = str(item["entity"]["id"])
        entry = [
            build_name_translation(entity_id, item["entity"]["name"]),
            build_badge_translation(entity_id, item["entity"]["badge"]["text"])
        ]
        if is_it_for_nl:
            entry.append(build_badge_translation(entity_id, item["entity"]["badge"]["text"], "nl_NL"))

        item['translations'] = entry
    else:
        for i in item['translations'][::-1]:
            if i["entityType"] not in ('MARKET_GROUP', 'MARKET_GROUP_BADGE'):
                item['translations'].remove(i)

        isOriginalTranslationAvailable = False
        for i in item['translations'][::-1]:
            if i["lang"] == 'original' and i["entityType"] == 'MARKET_GROUP':
                i["value"] = item["entity"]["name"]
                if isOriginalTranslationAvailable:
                    # remove duplicates of original translations
                    item['translations'].remove(i)
                isOriginalTranslationAvailable = True

        # Add original translation if not available
        if not isOriginalTranslationAvailable:
            id, v = (str(item["entity"]["id"]), item["entity"]["name"])
            item['translations'].append(build_name_translation(id, v))

        isOriginalTranslationAvailable = False
        isNLTranslationAvailable = False
        for i in item['translations']:
            if i["entityType"] == 'MARKET_GROUP_BADGE':
                if i["lang"] == 'original':
                    if isOriginalTranslationAvailable:
                        # remove duplicates of original translations
                        item['translations'].remove(i)
                    isOriginalTranslationAvailable = True
                elif i["lang"] == 'nl_NL':
                    if isNLTranslationAvailable:
                        # remove duplicates of original translations
                        item['translations'].remove(i)
                    isNLTranslationAvailable = True

        id = str(item["entity"]["id"])
        v = item["entity"]["badge"]["text"]

        # Add original translation if not available
        if not isOriginalTranslationAvailable:
            item['translations'].append(build_badge_translation(id, v))
        elif is_it_for_nl:
            item['translations'].append(build_badge_translation(id, v, "nl_NL"))


json_dump = json.dumps(parameters, indent=2)
open("out_" + file_name, 'w').write(json_dump)
