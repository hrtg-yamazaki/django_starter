import os
from pathlib import Path


os.chdir(Path(__file__).parent)


import MySQLdb
from time import sleep
from local_settings import DB_NAME, DB_USER, DB_PASSWORD


# どれくらい値は必要に応じて調整
count_to_try = 0
LIMIT_OF_COUNT = 20


def check_connection(count, limit):
    """
    docker-compose up実行時用、時間調整のための関数。
    
    (記事では以下は解説の雛形に使う => docstringからは除外したい)
    コンテナ「web」が先に立ち上がってしまった場合に、
    依存関係にあるコンテナ「db」の立ち上げまでの間、
    「python manage.py runserver」の実行を保留させる。

    「db」の立ち上げまでの待機時間が足りない場合は、
    LIMIT_OF_COUNTの値(接続を試行する回数の上限)を調整して実行。
    """

    try:
        conn = MySQLdb.connect(
            unix_socket = "/var/run/mysqld/mysqld.sock",
            user=DB_USER,
            passwd=DB_PASSWORD,
            host="db",
            port=3306,
            db=DB_NAME,
        )
    except MySQLdb._exceptions.OperationalError as e:
        count += 1
        print("Waiting for MySQL... (", count, "/ 20 )")
        sleep(3)
        if count < 20:
            check_connection(count, limit)
        else:
            print(e)
            print("Failed to connect mySQL.")
    else:
        print("Connected!\n")
        conn.close()
        exit()


if __name__ == "__main__":

    check_connection(count_to_try, LIMIT_OF_COUNT)
