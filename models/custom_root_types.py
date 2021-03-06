from typing import List
import json
from pydantic import BaseModel
from pydantic.schema import schema

class Pets(BaseModel):
    __root__: List[str]
    
print(Pets(__root__=['dog', 'cat']))
print()
print(Pets(__root__=['dog', 'cat']).json())
print()
print(Pets.parse_obj(['dog', 'cat']))
print()
print(Pets.schema())
print()
pets_schema = schema([Pets])
print(json.dumps(pets_schema, indent=4))