import json
from urllib import request
import pymongo
from pymongo import MongoClient
import requests

# cluster = MongoClient('localhost', 27017)

# db = cluster["dbbinance"]

# collection = db["bitcoin"]

# collection.insert_one({"test":"test"})


# data production ( Binance ) :

# Bitcoin Data 

url ="https://api1.binance.com/api/v3/trades"

param = {
    "symbol":"BTCUSDT"
}

requete = requests.get(url = url, params=param)

if(requete.status_code==200):
    print(requete.json())
else:
    print("error")
