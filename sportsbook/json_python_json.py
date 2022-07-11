import json

# JSON text
text = '{"MARKET_GROUP": ["name"], "MARKET_GROUP_BADGE": ["text"], "COUPON": ["name"], "MARKET_FILTER": ["name"], "SUB_CATEGORIES": ["name"], "WIDGET": ["name"], "EVENT_GROUP": ["name"], "MARKET_TYPE": ["selectionNameTemplate"], "BET_BUILDER_MARKET_GROUP": ["displayText"], "BET_BUILDER_MARKET_GROUP_FILTER_OPTION": ["displayText"], "QUICK_LINK": ["name"], "MARKET_FILTER_SELECTION": ["name"], "CATEGORIES": ["name"], "VIRTUAL_CONFIGURATION": ["name"], "MESSAGE": ["name", "text"], "BET_BUILDER_MARKET_GROUP_FILTER": ["defaultOption"], "BANNER": ["tacTitle"], "QUICK_LINK_BADGE": ["text"], "PROMOTION": ["title", "shortDescription", "fullDescription", "keyInformation", "tacDescription", "keyInformationTitle", "tacDescriptionTitle"], "PROMOTION_CTA_STEP": ["text", "finalText", "title", "finalTitle"], "TOP_ACCA_GROUP": ["name"], "PROMOTION_CTA_STEP_BUTTON": ["name"], "MORE_PAGE": ["name"], "BET_BUILDER_ACCA": ["name"], "EVENT_NOTE": ["eventNotes", "eventTitle"], "MESSAGE_BUTTON": ["name"]}'

# Sorted dict
dict = dict(sorted(json.loads(text).items()))

# dump to JSON text
text = json.dumps(dict)
print(text)
