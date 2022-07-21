import json


file_name = "UserSettings.json"
out = []
with open(file_name, "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        dict = json.loads(line)
        if "liveAlerts" in dict:
            live_alerts = dict["liveAlerts"]
            if live_alerts and "defaultHappenings" in live_alerts:
                default_happenings = live_alerts["defaultHappenings"]
                if len(default_happenings) > 6:
                    out.append(dict["_id"])

json_dump = json.dumps(out)
with open("out.json", 'w') as f:
    f.write(json_dump)
