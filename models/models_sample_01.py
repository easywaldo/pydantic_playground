from typing import List
from pydantic import BaseModel, constr

"""
pydantic dict()
    returns a dictionary of the model's fields and values; cf. exporting models
    

"""

class User(BaseModel):
    id: int
    name = 'easywaldo'
    

class Foo(BaseModel):
    count: int
    size: float = None
    
class Bar(BaseModel):
    apple = 'x'
    banana = 'y'
    

class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]
    
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))    

class CompayModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    domains: List[constr(max_length=255)]
    
    class Config:
        orm_mode = True


def main():
    user = User(id='123')
    assert user.id == 123
    assert user.name == 'easywaldo'
    assert user.__fields_set__ == {'id'}
    assert user.dict() == dict(user) == {'id': 123, 'name': 'easywaldo'}
    user.id = 999
    assert user.id == 999
    
    user_clone = user.copy()
    assert user_clone == user
    
    user_clone.id = 1000
    
    
    print(user.json())
    print(user_clone.json())
    
    # assert user_clone == user
    
    print(user.schema())
    print(user.schema_json())
    print('construct() ================================')
    print(user_clone.construct())
    print('__fields__ =================================')
    print(user_clone.__fields__)
    
    m = Spam(foo={'count': 100}, bars=[{'apple': 'x1'}, {'banana': 'y1'}])
    print(m)
    print(m.dict())
    
    
    
    co_orm = CompanyOrm(
        id=123,
        public_key='testing orm mode',
        domains=['fastapi.org', 'django.org']
    )
    print('co_orm =============================')
    print(co_orm)
    co_model = CompayModel.from_orm(co_orm)
    print('co_model =============================')
    print(co_model)

if __name__ == '__main__':
    main()