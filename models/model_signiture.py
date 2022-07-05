import inspect
from pydantic import BaseModel, Field

class FooModel(BaseModel):
    id: int
    name: str = None
    description: str = 'Foo'
    apple: int = Field(..., alias='pear')
    
print(inspect.signature(FooModel))




class MyModel(BaseModel):
    id: int
    info: str = 'Foo'
    
    def __init__(self, id: int = 1, *, bar: str, **data) -> None:
        """My custom int"""
        super().__init__(id=id, bar=bar, **data)

print(inspect.signature(MyModel))