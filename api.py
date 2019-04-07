import json
import requests
import os

URL = "https://developers.zomato.com/api/v2.1/"
KEY = "9d83b19463fa5f6cf94b1af9f5ca17fa"
HEADER = {"user-key": KEY}
ESTABLISHMENT = "establishments?city_id="
CATEGORY = "categories"
CUISINE = "cuisines?city_id="
SEARCH = "search"

city_id = 65  # id for jozi
s = "search?entity_type=city&q=Johannesburg&sort=rating&order=desc"
search = "search?entity_type={}&q={}&sort=rating&order=desc"
entity_type = "city"  # search by
entity_name = "Johannesburg"
param = {
    'city_id': city_id,
    'q': 'mushroom'
}


def get_resource(end_point=None, p=None):
    response = requests.get(URL + end_point, params=p, headers=HEADER)
    return response


def get_establishments():
    exist = os.path.isfile("establishment.csv")
    if exist:
        return  # return file
    res = get_resource(ESTABLISHMENT + str(city_id))
    if res.status_code == 200:
        data = res.json()
        return json.dumps(data, indent=2, sort_keys=True)


def get_categories():
    exist = os.path.isfile("categories.csv")
    if exist:
        return  # return file
    res = get_resource(CATEGORY)
    if res.status_code == 200:
        data = res.json()
        return json.dumps(data, indent=2, sort_keys=True)
        # for category in data['categories']:
        #     print (category['categories'])


def get_cuisines():
    exist = os.path.isfile("cuisines.csv")
    if exist:
        return  # return file
    res = get_resource(CUISINE + str(city_id))
    if res.status_code == 200:
        data = res.json()
        return json.dumps(data, indent=2, sort_keys=True)


def get_restaurants(typ, name):
    exist = os.path.isfile("restaurant.csv")
    if exist:
        return  # return file
    res = get_resource(search.format(typ, name))
    if res.status_code == 200:
        data = res.json()
        return json.dumps(data, indent=2)


def get_rest():
    res = get_resource(SEARCH, param)
    data = res.json()
    return json.dumps(data, indent=2, sort_keys=True)


def write_response_to_file():
    res = get_resource(SEARCH, param)
    if res.status_code == 200:
        data = res.json()
        with open('restaurant.json', 'w') as restaurant:
            json.dump(data, restaurant, indent=2)


