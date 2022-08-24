from typing import NamedTuple

from pydantic import BaseModel, ValidationError

class Point(NamedTuple):
    x: int
    y: int
    
    
class Model(BaseModel):
    p: Point
    

print(Model(p=('1', '2')))

try:
    Model(p=('1.3', '2'))
except ValidationError as e:
    print(e)
    
    
class NameCard(NamedTuple):
    x: str
    y: int
    

class NameModel(BaseModel):
    m: NameCard

print(NameModel(m=("easywaldo", 42)))

try:
    NameModel(m=("easywaldo", "h2"))
except ValidationError as e:
    print(e)