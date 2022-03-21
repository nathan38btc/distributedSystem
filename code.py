import pymongo
from pymongo import MongoClient

cluster = MongoClient('localhost', 27017)

db = cluster["dbbinance"]

collection = db["bitcoin"]

collection.insert_one({"test":"test"})
