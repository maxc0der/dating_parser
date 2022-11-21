import sqlite3
import traceback
import sys
import time


def init():
    try:
        sqlite_connection = sqlite3.connect('base.db')
        sqlite_create_table_query = '''CREATE TABLE profiles (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    age INT NOT NULL,
                                    caption text NOT NULL,
                                    photo text NOT NULL,
                                    localphoto text NOT NULL,
                                    date datetime);'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def store(name, age, caption, photo, local_photo):
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")

        sqlite_insert_query = "INSERT INTO profiles(name, age, caption, photo, localphoto, date)  VALUES  ('{}', {}, '{}', '{}', '{}', {})".format(name, age, caption, photo, local_photo, time.time())
        print(sqlite_insert_query)
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

