import pickle
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name = 'easywaldo'
    signup_date: datetime = None
    
m = User.parse_obj({'id': 1334, 'name': 'john'})
print(m)

try:
    User.parse_obj(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)
    
m = User.parse_raw('{"id": 1334, "name": "john"}')
print(m)

pickle_data = pickle.dumps({
    'id': 1334,
    'name': 'john wadlo',
    'signup_date': datetime(2022, 6, 24)
})
m = User.parse_raw(pickle_data, content_type='application/pickle', allow_pickle=True)
print(m)

path = Path('data.json')
path.write_text('{"id": 1334, "name": "easywaldo"}')
m = User.parse_file(path)
print(m)