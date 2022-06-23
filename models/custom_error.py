from pydantic import BaseModel, ValidationError, validator

class Model(BaseModel):
    department_name: str
    
    @validator('department_name')
    def value_should_include_squad(cls, v: str):
        if not v.endswith('squad'):
            raise ValidationError('value should include squad')
        return v

try:
    Model(department_name='payment')
except ValidationError as e:
    print(e.errors())