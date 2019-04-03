import requests
import json
import urllib

MY_CSV = "food_coded_temp.csv"

def open_user_file():
    with open(MY_CSV) as meals:
        print (meals.read())

open_user_file()

