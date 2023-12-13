from pymongo import MongoClient

settings = {
    "ip": "mongodb://your_database",
    "db_name": "park_sys",
}
conn = MongoClient(settings['ip'])
db = conn[settings['db_name']]

if __name__ == '__main__':
    res = db.sys.find({})
    print(list(res))
    for item in res:
        item = dict(item)
        item.pop('_id')
        print(dict(item))
