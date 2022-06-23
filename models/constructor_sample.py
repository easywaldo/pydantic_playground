from pydantic import BaseModel

class User(BaseModel):
    id: int
    age: int
    name: str = 'easywaldo'
    
origin_user = User(id=132, age=42)

user_data = origin_user.dict()
print(user_data)

fields_set = origin_user.__fields_set__
print(fields_set)

new_user = User.construct(_fields_set=fields_set, **user_data)
print(new_user.__fields_set__)

bad_user = User.construct(id='other one')
print(repr(bad_user))