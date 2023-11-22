from app_flask.config.mysqlconnections import connectToMySQL
from app_flask import DATA_BASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    @classmethod
    def create_one(cls, data):
        query = """
                INSERT INTO users(first_name, last_name, email)
                VALUE (%(first_name)s, %(last_name)s, %(email)s);
                """
        return connectToMySQL(DATA_BASE).query_db(query, data)
    
    @classmethod
    def obtain_all(cls):
        query = """
                SELECT * FROM users;
                """
        result = connectToMySQL(DATA_BASE).query_db(query)
        users_list = []
        for row in result:
            print(row)
            current_user = cls(row)
            user = {
                **row,
                'id' : row['id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            current_user.user = User(user)
            users_list.append(current_user)
        return users_list
    
    @classmethod
    def delete_one(cls, data):
        query = """
                DELETE FROM users
                WHERE id = %(id)s;
                """
        return connectToMySQL(DATA_BASE).query_db(query, data)
    
    @classmethod
    def update_one(cls, data):
        query = """
                UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s,  email = %(email)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(DATA_BASE).query_db(query, data)
    
    @classmethod
    def obtain_one(cls, data):
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        print(query)
        result = connectToMySQL(DATA_BASE).query_db(query, data)
        return cls(result[0])