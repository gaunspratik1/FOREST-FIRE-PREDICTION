import pymongo


def database_connect_mongoDB(limit):
    client = pymongo.MongoClient(
        "mongodb+srv://gaunspratik1:pymongo_1@cluster0.dczyoah.mongodb.net/?retryWrites=true&w=majority")
    db2 = client['FIRE']
    fire_coll = db2['fire_collection']
    j = []
    for i in fire_coll.find().limit(limit):
        raw_values = list(i.values())
        raw_values.pop(0)
        j.append(raw_values)
    return j
