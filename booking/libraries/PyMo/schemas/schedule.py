import datetime
from pymongoose import methods
from pymongoose.mongo_types import Types, Schema, MongoException, MongoError
from bson import json_util
from bson.objectid import ObjectId

schedules = None

def user_model_init (db):
   global schedules
   schedules = db["schedules"]

class Schedule(Schema):
    """
    Sets up the Schedule Schema
    """

    schema_name = "schedules"
    
    do_sch_id = None
    do_sch_date = None
    do_sch_category = None
    do_sch_time = None
    
    def __init__(self, **kwargs):
        req_string = {
                "type": Types.String,
                "required": True
            }

        self.schema = {
            "do_sch_date": req_string,
            "type_of_service": req_string,
        }

        super().__init__(self.schema_name, self.schema, kwargs)

    def __str__(self):
        return f"User: {self.name}, Actions: {self.action}"