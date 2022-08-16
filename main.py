from typing import List
from flask import request
from flask.views import MethodView
from app import app
from queries import DataQuery

class GroupAPI(MethodView):
    def get(self) -> List:
        data = DataQuery().get_data()
        return data
               
    def post(self) -> str:
        request_data = str(request.json.get("data"))
        request_data_bytes = request_data.encode('utf-8')
        DataQuery().create_data(request_data_bytes)
        return "Object was successfuly created!"

app.add_url_rule('/', view_func=GroupAPI.as_view('show_users'))