import py3_database


def test_redis_db():
    redis_db = py3_database.redis_db.RedisDB.from_uri("redis://:@localhost:6379/0?encoding=utf-8&decode_responses=True")
    print(redis_db.redis)

    redis_db = py3_database.redis_db.RedisDB(
        host="localhost",
        port=6379,
        password=None,
        dbname=0
    )
    print(redis_db.redis)


if __name__ == '__main__':
    test_redis_db()
