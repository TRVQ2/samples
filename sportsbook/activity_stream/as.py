import requests
import json
import csv
from datetime import datetime


def get_data(file, url, session_id):
    response = requests.get(
        url,
        cookies={'JSESSIONID': session_id},
        allow_redirects=False
    ).text

    with open(file, "w", encoding="utf-8") as f:
        f.write(response)


def filter_data(file_in, file_out="out_filtered"):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    out = []
    for i in data:
        if i["username"] == "youri.smit":
            if "action" in i:
                parts = i["action"].split(' Body : ')
                if len(parts) > 1:
                    body = json.loads(parts[1]) if len(parts[1]) > 0 else None
                    i["action"] = {"message": parts[0], "body": body}
                else:
                    body = i["action"]
                    if len(body) > 0:
                        try:
                            body = json.loads(body)
                        except Exception:
                            pass
                        i["action"] = {"body": body}
            i["datetime"] = str(datetime.fromtimestamp(i["timestamp"]))
            out.append(i)
    json_dump = json.dumps(out, indent=2)
    with open(file_out + ".json", "w", encoding="utf-8") as f:
        f.write(json_dump)

    with open(file_out + ".csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, delimiter='\t', fieldnames=out[0].keys())
        writer.writeheader()
        for i in out:
            writer.writerow(i)


if __name__ == "__main__":
    url = "https://sportsadmin.virginbet.com/api/betting/nl/v1/activity/" + \
        "log/list?startTime=1657704817&endTime=1658309617"
    session_id = "FC2D71FDACB9614CAE95F65AD07F9CDE"
    file_name = "in.json"
    # get_data(file_name, url, session_id)
    filter_data(file_name)
