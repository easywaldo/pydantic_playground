from typing_extensions import TypedDict

from pydantic import BaseModel, Extra, ValidationError

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
