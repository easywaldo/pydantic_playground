from pydantic import BaseModel, create_model

DynamicFooBarModel = create_model('DynamicFooBarModel', foo=(str, ...), bar=123)

class StaticFooBarModel(BaseModel):
    foo:str
    bar: int = 123