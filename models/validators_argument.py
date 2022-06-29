from pydantic import create_model, ValidationError, validator

def username_alphanumeric(cls, v):
    assert v.isalnum(), 'must be alphanumeric'
    return v

validators = {
    'username_validator':
        validator('username')(username_alphanumeric)
}

UserModel = create_model('UserModel',
                         username=(str, ...),
                         __validators__=validators)

user = UserModel(username='waldo')
print(user)

try:
    UserModel(username='waldo999%n')
except ValidationError as e:
    print(e)