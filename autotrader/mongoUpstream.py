import pymongo
import uuid

client = pymongo.MongoClient("localhost", 27017)
db = client["TheHoarder"]

