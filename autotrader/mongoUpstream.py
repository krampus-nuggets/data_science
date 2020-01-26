import pymongo
import uuid

client = pymongo.MongoClient("localhost", 27017)
db = client["TheHoarder"]

dummyCars = [
    {
        "autotrader_id": "autotrader-{}".format(uuid.uuid4()),
        "site": "autotrader.co.za",
        "brand": "Audi",
        "title": "2010 Audi A3 3-Door 1.8T Ambition",
        "area": "Montague Gardens",
        "price": "R 78 000",
        "range": "R50k to R100k"
    },
    {
        "autotrader_id": "autotrader-{}".format(uuid.uuid4()),
        "site": "autotrader.co.za",
        "brand": "Audi",
        "title": "2008 Audi A4 1.8T Ambition",
        "area": "Montague Gardens",
        "price": "R 60 000",
        "range": "R50k to R100k"
    },
    {
        "autotrader_id": "autotrader-{}".format(uuid.uuid4()),
        "site": "autotrader.co.za",
        "brand": "BMW",
        "title": "2010 BMW 1 Series 120i Convertible Auto",
        "area": "Montague Gardens",
        "price": "R 169 900",
        "range": "R100k to R200k"
    }
]

