from typing_extensions import TypedDict

from pydantic import BaseModel, Extra, ValidationError, HttpUrl, PostgresDsn, validator

class UserIdentity(TypedDict, total=False):
    name: str
    sur_name: str
    
    
class User(TypedDict):
    identity: UserIdentity
    age: int
    

class Model(BaseModel):
    u: User
    
    class Config:
        extra = Extra.forbid
        
m1 = Model(u={
    'identity': {'name': 'Smith', 'sur_name': 'John'}, 'age': '42'
})

m2 = Model(u={
    'identity': {'name': None, 'sur_name': 'John'}, 'age': '42'
})

m3 = Model(u={
    'identity': {}, 'age': '42'
})


print(m1)
print(m2)
print(m3)

try:
    Model(u={'identity': {'name': ['easy', 'waldo'], 'sur_name': 'John'}, 'age': '42'})
except ValidationError as e:
    print(e)
    

try:
    Model(
        u={
            'identity': {'name': 'Smith', 'sur_name': 'John'}, 'age': '42', 'email': 'john@example.com',
        }
    )
except ValidationError as e:
    print(e)


class MyModel(BaseModel):
    url: HttpUrl
    
m = MyModel(url="http://example.com")
print(m.url)

try:
    MyModel(url="ftp://invalid.url")
except ValidationError as e:
    print(e)
    

try:
    MyModel(url="not a url")
except ValidationError as e:
    print(e)
    
    
class MyDatabaseModel(BaseModel):
    db: PostgresDsn
    
    @validator('db')
    def check_db_name(cls, v):
        assert v.path and len(v.path) > 1, 'database must be provided'
        return v
    

m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
print(m.db)

try:
    MyDatabaseModel(db='postgres://user:pass@localhost:5432')
except ValidationError as e:
    print(e)
