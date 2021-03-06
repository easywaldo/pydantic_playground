from typing import Literal, Union
from typing_extensions import Annotated

from pydantic import BaseModel, Field, ValidationError

class BlackCat(BaseModel):
    pet_type: Literal['cat']
    color: Literal['black']
    black_name: str
    
class WhiteCat(BaseModel):
    pet_type: Literal['cat']
    color: Literal['white']
    white_name: str
    
Cat = Annotated[Union[BlackCat, WhiteCat], Field(discriminator='color')]

class Dog(BaseModel):
    pet_type: Literal['dog']
    name: str
    
Pet = Annotated[Union[Cat, Dog], Field(discriminator='pet_type')]

class Model(BaseModel):
    pet: Pet
    n: int
    
m = Model(pet={'pet_type': 'cat', 'color': 'black', 'black_name': 'dodo'}, n=1)
print('================================')
print(m)

try:
    Model(pet={'pet_type':'cat', 'color': 'red'}, n=1)
except ValidationError as e:
    print(e)
    
try:
    Model(pet={'pet_type': 'cat', 'color': 'black'}, n=1)
except ValidationError as e:
    print(e)