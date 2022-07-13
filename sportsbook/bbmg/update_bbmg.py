import requests
import json


def send_get_request(url):
    response = requests.get(url, allow_redirects=False).text
    return json.loads(response)


def update_bbmg_list(url, list, env, brand):
    post_url = "https://dev-admin.virginbet.com/api/betting/ls/v1/betbuilder/marketgroups"
    failed_cases = []
    for i in list:
        body = {}
        id = i["id"]
        i.pop("id")
        body["entity"] = i
        body["translations"] = send_get_request("https://dev-admin.virginbet.com/api/betting/vb/v1/translator/{}".format(id))
        print(f"Processing bbmg '{id}'. Sending request...")
        response = requests.post(
            f"{post_url}",
            json=body
        )
        status_code = response.status_code
        print(f"Status code: {status_code}")
        if status_code != 200:
            failed_cases.append({"id": id, "status_code": status_code})
            print(response)
            break
    print("Failed cases:\n" + '\n'.join(str(x) for x in failed_cases))
    return failed_cases



def import_bbmg(brand, env, session):
    with open('config.json', 'r') as f:
        parameters = json.loads(f.read())
    brands = parameters['brands']
    envs = parameters['envs']
    get_url = parameters['get_all_bbmg_url']
    bbmgs = send_get_request(get_url)
    post_url = parameters['update_bbmg_url']
    update_bbmg_list(post_url, bbmgs, envs[env], brands[brand])


def main():
    brands = ["vb", "vbuk", "uk", "ng", "nl"]
    brands = ["uk"]
    env = "dev"
    session = ''
    for i in brands:
        import_bbmg(i, env, session)


if __name__ == "__main__":
    main()
