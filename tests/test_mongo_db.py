import py3_database


def test_mongo_db():
    mongo_db = py3_database.mongo_db.MongoDB.from_uri("mongodb://localhost:27017/py3_database")
    print(mongo_db.client)

    mongo_db = py3_database.mongo_db.MongoDB(
        host="localhost",
        port=27017,
        username=None,
        password=None,
        dbname="py3_database"
    )
    print(mongo_db.client)


if __name__ == '__main__':
    test_mongo_db()
