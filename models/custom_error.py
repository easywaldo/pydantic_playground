from pydantic import BaseModel, ValidationError, validator, PydanticValueError

class NotMatchError(PydanticValueError):
    code = 'not_match_error'
    msg_template = 'value is not include squad, {wrong_value}'

class Model(BaseModel):
    department_name: str
    
    @validator('department_name')
    def value_should_include_squad(cls, v: str):
        if not v.endswith('squad'):
            # raise ValidationError('value should include squad')
            raise NotMatchError(wrong_value=v)
        return v

try:
    Model(department_name='payment')
except ValidationError as e:
    print(e.errors())