import datetime
from pymongoose import methods
from pymongoose.mongo_types import Types, Schema, MongoException, MongoError
from bson import json_util
from bson.objectid import ObjectId

users = None

def user_model_init (db):
   global users
   users = db["users"]

class User(Schema):
    """
    Sets up the User Schema
    """
    
    schema_name = "users"

    id = None
    signup_name = None
    email = None
    mobile = None
    password = None
    birthdate = None
    
    def __init__(self, **kwargs):
        req_string = {
                "type": Types.String,
                "required": True
            }

        self.schema = {
            "signup_name": req_string,
            "email": req_string,
            "mobile": req_string,
            "password": req_string,
            "birthdate": req_string
        }

        super().__init__(self.schema_name, self.schema, kwargs)

    def __str__(self):
        return f"User: {self.signup_name}, Email: {self.email}, Mobile: {self.mobile}, Password: {self.password}, Birthdate: {self.birthdate}"
    
    def getID(self):
        return self.id
    
    def getEmail(self):
        return self.email