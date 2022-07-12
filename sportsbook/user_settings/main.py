import json


file_name = "UserSettings.json"
file = open(file_name, "r")
out = []
while True:
    line = file.readline()
    if not line:
        break
    dict = json.loads(line)
    if "liveAlerts" in dict:
        live_alerts = dict["liveAlerts"]
        if "defaultHappenings" in live_alerts:
            default_happenings = live_alerts["defaultHappenings"]
            if len(default_happenings) > 6:
                out.append(dict["_id"])
file.close()

json_dump = json.dumps(out)
open("out.json", 'w').write(json_dump)
