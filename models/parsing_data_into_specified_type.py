from typing import List

from pydantic import BaseModel, parse_obj_as

class Item(BaseModel):
    id: int
    name: str

item_data = [{'id': 1, 'name': 'easywaldo'}]

items = parse_obj_as(List[Item], item_data)
print(items)


wrong_item_data = {'id': 100,}
items = parse_obj_as(List[Item], [wrong_item_data])
print(items)