import sqlite3
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True
    )
    parser.add_argument(
        'password',
        type=str,
        required=True
    )
    def post(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "insert into users values (null, ?,?)"
        data = UserRegister.parser.parse_args()
        cursor.execute(query, (data['username'], data['password'],))

        connection.commit()
        connection.close()

        return {"message": "successfully created a new user"}, 201


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "select * from users where username = ?"
        result = cursor.execute(query,(username,))

        row = result.fetchone()
        if row:
            #user = cls(row[0], row[1], row[2]) --> id, username, password
            user = cls(*row)
        else:
            user = None
        
        #connection.commit()
        connection.close()
        return user 
    
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "select * from users where id = ?"
        result = cursor.execute(query,(_id,))

        row = result.fetchone()
        if row:
            #user = cls(row[0], row[1], row[2]) --> id, username, password
            user = cls(*row)
        else:
            user = None
        
        #connection.commit()
        connection.close()
        return user 
