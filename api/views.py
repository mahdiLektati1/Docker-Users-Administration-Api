from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text


class UsersCollection(Resource):
    """ The Users Collection View """

    def __init__(self):
        self.db = Db()
    
    def get(self):
        """ Returns a list of users """
        query = "SELECT * FROM users ORDER BY created DESC"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        users = self.db.clean_select_results(rows, keys)

        return {
            'users': users
        }

    def post(self):
        """
        Add a user to the db 
        Expect a JSON payload with the following format
        {
            "firstname": "The first name of user",
            "name": "The last name of user",
            "email": "The adress email of user"
        }
        """
        data = request.get_json()
        query = "INSERT INTO `users` (`firstname`, `name`, `email`) VALUES (:firstname, :name, :email)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False


class UserItem(Resource):
    """ The User Item View """

    def __init__(self):
        self.db = Db()
    
    
    def get(self, user_id):
        """ Returns a user """
        data = { "id": user_id }
        query = "SELECT * FROM `users` WHERE `id` = :id"
        res = self.db.connection.execute(sql_text(query), data)
        rows = res.fetchall()
        keys = res.keys()
        user = self.db.clean_select_results(rows, keys)
        if ( user is not None and len(user) > 0):
            return user[0]
        else:
            return False

    def put(self, user_id):
        """
        Update a user in the db 
        Expect a JSON payload with the following format
        {
            "firstname": "The first name of user",
            "name": "The last name of user",
            "email": "The adress email of user"
        }
        """
        data = request.get_json()
        data["id"] = user_id
        query = "UPDATE `users` SET `firstname` = :firstname, `name` = :name, `email` = :email WHERE `id` = :id"
        
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False
    
    def delete(self, user_id):
        """
        Delete a user from the db 
        Expect user id in url params
        """
        data = { "id": user_id }
        query = "DELETE FROM `users` WHERE `id` = :id"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False
