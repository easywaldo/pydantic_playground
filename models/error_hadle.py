from typing import List
from pydantic import BaseModel, ValidationError, conint

class Location(BaseModel):
    lat = 0.1
    lng = 10.1
    
class LocationModel(BaseModel):
    is_required: float
    gt_int: conint(gt=42)
    list_of_ints: List[int] = None
    a_float: float = None
    recursive_model: Location = None
    
loc_data = dict(
    list_of_ints=['1', 2, 'bad'],
    a_float='not a float',
    recursive_model={'name': 'waldo'},
    gt_int=41,
)

try:
    LocationModel(**loc_data)
except ValidationError as e:
    print(e)
    print(e.json())