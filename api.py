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
    exist = os.path.isfile("establishment.json")
    if exist:
        return read_data_from_file("establishment.json")
    res = get_resource(ESTABLISHMENT + str(city_id))
    if res.status_code == 200:
        data = res.json()
        write_response_to_file("establishment.json", data)
        return json.dumps(data, indent=2, sort_keys=True)


def get_categories():
    exist = os.path.isfile("categories.json")
    if exist:
        return read_data_from_file("categories.json")
    res = get_resource(CATEGORY)
    if res.status_code == 200:
        data = res.json()
        write_response_to_file("categories.json", data)
        return json.dumps(data, indent=2, sort_keys=True)
        # for category in data['categories']:
        #     print (category['categories'])


def get_cuisines():
    exist = os.path.isfile("cuisines.json")
    if exist:
        return read_data_from_file("cuisines.json")
    else:
        res = get_resource(CUISINE + str(city_id))
        if res.status_code == 200:
            data = res.json()
            write_response_to_file("cuisines.json", data)
            return json.dumps(data, indent=2, sort_keys=True)


def get_restaurants():
    exist = os.path.isfile("restaurant.json")
    if exist:
        return read_data_from_file("restaurant.json")
    else:
        res = get_resource(SEARCH, param)
        if res.status_code == 200:
            data = res.json()
            write_response_to_file("restaurant.json", data)
            return json.dumps(data, indent=2, sort_keys=True)


def write_response_to_file(file_name, data):
    with open(file_name, 'w') as write_file:
        json.dump(data, write_file, indent=2, sort_keys=True)


def read_data_from_file(file_name):
    with open(file_name, "r") as read_file:
        return json.load(read_file)


# def get_rest(typ, name):
#     exist = os.path.isfile("restaurant.csv")
#     if exist:
#         return  # return file
#     res = get_resource(search.format(typ, name))
#     if res.status_code == 200:
#         data = res.json()
#         return json.dumps(data, indent=2)
