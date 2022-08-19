from schemas import DataObject
from models import Data

def get_readable_data(data_object:Data) -> dict:
        pydantic_data = DataObject(id=data_object.id,data=data_object.data.decode("utf-8"))
        readable_data = pydantic_data.dict()
        return readable_data

def get_single_data_response(id=None,data=None,link=None) -> dict:
    response_data = {
            "data": {
                "type":"data",
                "id":id,
                "attributes":{
                    "data":data
                }
            },
            "links": {
                "self": link
            }
        }

    return response_data