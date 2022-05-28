from pydantic import BaseModel

"""
pydantic dict()
    returns a dictionary of the model's fields and values; cf. exporting models
    

"""

class User(BaseModel):
    id: int
    name = 'easywaldo'


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
    
    assert user_clone == user

if __name__ == '__main__':
    main()