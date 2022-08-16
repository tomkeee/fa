from typing import List
from models import Data
from database import session

class DataQuery:
    def create_data(self, request_data) -> Data:
        new_object = Data(data=request_data)
        session.add(new_object)
        session.commit()
        session.refresh(new_object)
        return new_object
    
    def get_data(self) ->List[Data]:
        data_from_db = session.query(Data).all()

        objects = []
        for object in data_from_db:
            obj = {
                "id":object.id,
                "data":object.data.decode("utf-8")
            }
            objects.append(obj)
        
        return objects