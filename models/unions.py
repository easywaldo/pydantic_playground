from uuid import UUID
from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    id: Union[int, str, UUID]
    name: str
    
easy_waldo = User(id=1212, name='easywaldo')
print(easy_waldo)

print(easy_waldo.id)

user_02 = User(id='1234', name='foo')
print(user_02)
print(user_02.id)

user_03_uuid = UUID('cf57432e-809e-4353-adbd-9d5c0d733868')
user_03 = User(id=user_03_uuid, name='bar')
print(user_03)
print(user_03.id)
print(user_03_uuid.int)