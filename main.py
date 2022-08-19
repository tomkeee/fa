from flask import request,json
from flask.views import MethodView
from flask import Response

from queries import DataQuery
from utils import get_readable_data,get_single_data_response

class GroupAPI(MethodView):
    def get(self) -> Response:
        data_objects = DataQuery().get_all_data()
        
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
        
        return Response(response=json.dumps(response_data),status=200,mimetype='application/json')
               
    def post(self) -> Response:
        if request.json.get("data") is None:
            return Response(status=204)
        try:
            created_object = DataQuery().create_data(request.json)
            response_data = get_single_data_response(id=created_object.id,data=created_object.data.decode("utf-8"),link="http://localhost:8080")
            return Response(response=json.dumps(response_data),status=201,mimetype='application/json')
        except:
            return Response(status=403)

            
        
class DataCRUD(MethodView):
    def get(self,id) -> Response:
        data = DataQuery().get_data_by_id(id)
        if data:
            readable_data = get_readable_data(data)
            response_data = get_single_data_response(id=readable_data.get("id"),data=readable_data.get("data"),link=f"http://localhost:8080/{id}")
            return Response(response=json.dumps(response_data),status=200,mimetype='application/json')
        return Response(status=404)
        
    
    def delete(self,id) -> Response:
        deleted_data = DataQuery().delete_data(id)
        if deleted_data:
            return Response(status=204)
        return Response(status=404)

    def patch(self,id) -> Response:
        if request.json.get("data") is None:
            return Response(status=204)
        
        try:
            updated_data = DataQuery().update_data(id,request.json)
        except:
            return Response(status=403)
        
        if updated_data is None:
            return Response(status=404)
        

        readable_data = get_readable_data(updated_data)
        response_data = get_single_data_response(id=readable_data.get("id"),data=readable_data.get("data"),link=f"http://localhost:8080/{id}")
        return Response(response=json.dumps(response_data),status=201,mimetype='application/json')
        