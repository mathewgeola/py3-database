import os

import py3_database


def test_mysql_db():
    mysql_db = py3_database.mysql_db.MysqlDB.from_uri("mysql+pymysql://root:root@127.0.0.1:3306/?charset=utf8mb4")
    print(mysql_db.connection)

    # language=mysql
    sql = "CREATE DATABASE IF NOT EXISTS `py3_database` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';"
    mysql_db.execute(sql)

    mysql_db = py3_database.mysql_db.MysqlDB(
        host="localhost",
        port=3306,
        username="root",
        password="root",
        dbname="py3_database",
        charset="utf8mb4"
    )
    print(mysql_db.connection)

    # language=mysql
    sql = """
          CREATE TABLE IF NOT EXISTS users
          (
              id
              INT
              AUTO_INCREMENT
              PRIMARY
              KEY,
              name
              VARCHAR
          (
              50
          ) NOT NULL,
              age INT NOT NULL,
              status VARCHAR
          (
              20
          ) DEFAULT 'active',
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) ENGINE = InnoDB
              DEFAULT CHARSET = utf8mb4;
          """
    print(mysql_db.execute(sql))

    sql = "INSERT INTO users (name, age, status) VALUES (%s, %s, %s);"
    params = [
        ("Alice", 20, "active"),
        ("Bob", 25, "active"),
        ("Charlie", 30, "inactive"),
        ("David", 22, "active"),
        ("Eve", 28, "inactive"),
    ]
    print(mysql_db.executemany(sql, params))

    excel_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.xlsx")
    sql = "select * from users;"
    df = mysql_db.query(sql, use_new_connect=True, return_df=True)
    df.to_excel(excel_file_path, index=False)

    sql = "select * from users where id = %s;"
    param = (1,)
    rows = mysql_db.query(sql, param)
    print(rows)

    sql = "select * from users where id = %(id)s;"
    param = dict(id=3)
    rows = mysql_db.query(sql, param)
    print(rows)


if __name__ == '__main__':
    test_mysql_db()
