from typing import Type

from pydantic import BaseModel
from pydantic import ValidationError

class Foo:
    def __init__(self, name: str):
        self.name = name

class Bar(Foo):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = description

class Other:
    def __init__(self, name: str, description: str, etc: str):
        self.name = name
        self.description = description
        self.etc = etc

class SimpleModel(BaseModel):
    just_subclasses: Type[Foo]
    
SimpleModel(just_subclasses=type(Foo(name="foo")))
SimpleModel(just_subclasses=type(Bar(name="waldo", description="desc")))

try:
    SimpleModel(just_subclasses=type(Other(name="wrong", description="none", etc="etc")))
except ValidationError as e:
    print(e)