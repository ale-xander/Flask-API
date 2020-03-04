import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?,?,?)"
users = [
    (1, 'alice', 'haha'),
    (2, 'bascom', 'lol'),
    (3, 'charlie', 'idgaf'),
    (4, 'dumas', 'wtf')
]
cursor.executemany(insert_query, users)

connection.commit()
connection.close()
