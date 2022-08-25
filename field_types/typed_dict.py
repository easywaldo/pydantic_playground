from typing_extensions import TypedDict

from pydantic import BaseModel, Extra, ValidationError, HttpUrl, PostgresDsn, validator, SecretStr, SecretBytes
from pydantic.color import Color

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


c = Color('ff00ff')
print(c.as_named())

print(c.as_hex())

c2 = Color('green')
print(c2.as_rgb_tuple())

print(c2.original())
print(repr(Color('hsl(180, 100%, 50%)')))

class ColorModel(BaseModel):
    color: Color
    
try:
    ColorModel(color='hello')
except ValidationError as e:
    print(e)


class SimpleModel(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes
    
sm = SimpleModel(password='easy_waldo', password_bytes=b'easy_waldo')
print(sm)
print(sm.password)
print(sm.dict())

try:
    SimpleModel(password=[1,2,3], password_bytes=[1,2,3])
except ValidationError as e:
    print(e)
    
class SimpleModelDumpable(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes
    
    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None,
            SecretBytes: lambda v: v.get_secret_value() if v else None,
        }

sm2 = SimpleModelDumpable(password='easy_waldo', password_bytes=b'easy_waldo')
print(sm2)
print(sm2.password)
print(sm2.dict())
print(sm2.json())
