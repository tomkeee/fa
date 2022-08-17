from flask import request
from flask.views import MethodView

from typing import List
from queries import DataQuery

class GroupAPI(MethodView):
    def get(self) -> dict:
        data_objects = DataQuery().get_data()
        
        data_object_list = []
        
        for data in data_objects:
            data_object = {
                "type":"data",
                "id":data.get("id"),
                "attributes":{
                    "data":data.get('data')
                }
            }
            data_object_list.append(data_object)
        
        response_data = {
            "data":data_object_list,
            "links": {
                "self": "http://localhost:8080/"
            }
        }
        
        return response_data
               
    def post(self) -> dict:
        request_data = str(request.json.get("data"))
        request_data_bytes = request_data.encode('utf-8')
        
        created_object = DataQuery().create_data(request_data_bytes)
        
        response_data = {
            "links": {
                "self": "http://localhost:8080/"
            },
            "data":{
                "type":"data",
                "id":created_object.id,
                "attributes":{
                    "data":created_object.data.decode("utf-8")
                }
            }
        }
        return response_data
        
class DataCRUD(MethodView):
    def get(self,*args,**kwargs):
        data = DataQuery().get_data_by_id(kwargs.get("id"))
        readable_data = DataQuery().get_readable_data(data)
        return {"data":readable_data}