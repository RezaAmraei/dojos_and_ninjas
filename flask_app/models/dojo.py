
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        
        for dojo in results:
            dojos.append ( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        print('------------------------------NEW LINE-----------------------------------------------')
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojo_id)s;"
        
        # query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        
        
        # results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos_with_ninjas = []
        
        for dojo in results:
            dojos_with_ninjas.append ( (dojo) )
            print("///////////////////////////////////////////////",dojo, "////////////////////////////")
        return dojos_with_ninjas
        # return cls(results[0])