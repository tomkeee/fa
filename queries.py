from typing import List
from models import Data
from database import session
from schemas import DataObject,DateInput

class DataQuery:
    def create_data(self, request_data:dict) -> Data:
        new_data = DateInput(data=str(request_data.get("data")).encode("utf-8")).dict()
        new_object = Data(data=new_data.get('data'))
        session.add(new_object)
        session.commit()
        session.refresh(new_object)
        return new_object
    
    def get_all_data(self) ->List[Data]:
        data_from_db = session.query(Data).all()

        objects = []
        for object in data_from_db:
            pydantic_data = DataObject(id=object.id,data=object.data.decode("utf-8"))
            objects.append(pydantic_data.dict())
        
        return objects
    
    def get_data_by_id(self,data_id:int) -> Data:
        data_from_db = session.query(Data).filter(Data.id == data_id).first()
        return data_from_db

    def delete_data(self,data_id:int) -> Data:
        data_from_db = session.query(Data).filter(Data.id == data_id).first()
        if data_from_db:
            session.delete(data_from_db)
            session.commit()
        return data_from_db
    
    def update_data(self,data_id:int,request_data:dict) -> Data:
        new_data = DateInput(data=str(request_data.get("data")).encode("utf-8"))
        data_db = session.query(Data).filter(Data.id == data_id)
        if data_db.first():
            data_db.update(new_data.dict())
            session.query(Data).filter(Data.id == data_id).update(new_data.dict())
            session.commit()

            updated_data = self.get_data_by_id(data_id)
            return updated_data
        return None