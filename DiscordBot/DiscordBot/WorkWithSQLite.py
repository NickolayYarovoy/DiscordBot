import sqlite3

sqlite_connection = sqlite3.connect(r'Data\DataBase\sqlite_python.db')

def create_user(user_id: int):
    cursor = sqlite_connection.cursor()

    sqlite_select_query = fr'''INSERT INTO users (user_id, respect, warns, last_respect_data) VALUES ({user_id}, 0, 0, 0)'''

    cursor.execute(sqlite_select_query) 
    sqlite_connection.commit()
    cursor.close()

def user_info(user_id: int) -> list:
    cursor = sqlite_connection.cursor()

    sqlite_select_query = fr'''SELECT * from users
                             WHERE user_id = {user_id};'''

    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    cursor.close()
    if len(records) > 0:
        return records[0]
    else:
        create_user(user_id)
        sqlite_connection.commit()
        return user_info(user_id)

def write_user_info(user):
    cursor = sqlite_connection.cursor()

    sqlite_select_query = fr'''UPDATE users
                               SET respect = {user[1]}, warns = {user[2]}, last_respect_data = {user[3]}
                               WHERE user_id = {user[0]};'''

    cursor.execute(sqlite_select_query) 
    sqlite_connection.commit()
    cursor.close()



