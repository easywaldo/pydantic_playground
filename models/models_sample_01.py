from typing import List
from pydantic import BaseModel

"""
pydantic dict()
    returns a dictionary of the model's fields and values; cf. exporting models
    

"""

class User(BaseModel):
    id: int
    name = 'easywaldo'
    

class Foo(BaseModel):
    count: int
    size: float = None
    
class Bar(BaseModel):
    apple = 'x'
    banana = 'y'
    

class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


def main():
    user = User(id='123')
    assert user.id == 123
    assert user.name == 'easywaldo'
    assert user.__fields_set__ == {'id'}
    assert user.dict() == dict(user) == {'id': 123, 'name': 'easywaldo'}
    user.id = 999
    assert user.id == 999
    
    user_clone = user.copy()
    assert user_clone == user
    
    user_clone.id = 1000
    
    
    print(user.json())
    print(user_clone.json())
    
    # assert user_clone == user
    
    print(user.schema())
    print(user.schema_json())
    print('construct() ================================')
    print(user_clone.construct())
    print('__fields__ =================================')
    print(user_clone.__fields__)
    
    m = Spam(foo={'count': 100}, bars=[{'apple': 'x1'}, {'banana': 'y1'}])
    print(m)

if __name__ == '__main__':
    main()