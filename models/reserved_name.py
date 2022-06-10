import typing

from pydantic import BaseModel, Field
import sqlalchemy as alchemy
from sqlalchemy.ext.declarative import declarative_base


class MyModel(BaseModel):
    metadata: typing.Dict[str, str] = Field(alias='metadata_')
    
    class Config:
        orm_mode = True

        
BaseModel = declarative_base()


class SQLModel(BaseModel):
    __tablename__= 'my_table'
    id = alchemy.Column('id', alchemy.Integer, primary_key=True)
    metadata_ = alchemy.Column('metadata', alchemy.JSON)
    

sql_model = SQLModel(metadata_={'key': 'val'}, id=1)

pydantic_model = MyModel.from_orm(sql_model)


print(pydantic_model.dict())
print(pydantic_model.dict(by_alias=True))