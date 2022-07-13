import requests
import os
import json
import string


def get_coupons_list(url):
    response = requests.get(url, allow_redirects=False).text
    return json.loads(response)["data"]


def update_coupons_list(url, list):
    failed_cases = []
    for i in list:
        uid = i["uid"]
        print(f"Processing coupon '{uid}'. Sending request...")
        i.pop("uid")
        response = requests.put(
            f"{url}/{uid}",
            json={"changeSet": i},
            allow_redirects=False
        )
        status_code = response.status_code
        print(f"Status code: {status_code}")
        if status_code != 200:
            failed_cases.append({"uid": uid, "status_code": status_code})

    print("Failed cases:\n" + '\n'.join(str(x) for x in failed_cases))
    return failed_cases


def update_coupons(list):
    for i in list:
        if 'marketFilterId' not in i:
            i['marketFilterId'] = None
            i['marketFilterIds'] = []
        elif i['marketFilterId'] is None:
            i['marketFilterIds'] = []
        elif 'marketFilterIds' not in i \
            or i['marketFilterIds'] is None \
                or i['marketFilterIds'] == []:
            i['marketFilterIds'] = [i['marketFilterId']]
    return list


def check_market_filters(list):
    for i in list:
        if 'marketFilterId' in i and i['marketFilterId'] is not None:
            print(f"uid={i['uid']}, marketFilterId={i['marketFilterId']}")
            print(f"uid={i['uid']}, marketFilterIds={i['marketFilterIds']}")
    return


def update_coupon_market_filters(brand, env, session):
    with open('config.json', 'r') as f:
        parameters = json.loads(f.read())
    brands = parameters['brands']
    envs = parameters['envs']
    get_url = parameters['get_all_coupons_url'] \
        .format(envs[env], brands[brand])
    coupons = update_coupons(get_coupons_list(get_url))
    post_url = parameters['update_coupon_url'] \
        .format(envs[env], brands[brand])
    # update_coupons_list(post_url, coupons)
    check_market_filters(coupons)


def main():
    brands = ["vb", "vbuk", "uk", "ng", "nl"]
    env = "dev"
    session = ''
    for i in brands:
        update_coupon_market_filters(i, env, session)


if __name__ == "__main__":
    main()
