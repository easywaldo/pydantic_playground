from typing import Type

from pydantic import BaseModel
from pydantic import ValidationError

class Foo:
    def __init__(self, name: str):
        self.name = name

class Bar(Foo):
    def __init__(self, name: str, description: str):
        super.name = name
        self.description = description

class Other:
    def _init(self, name: str, description: str, etc: str):
        super.name = name
        super.description = description
        self.etc = etc

class SimpleModel(BaseModel):
    just_subclasses: Type[Foo]
    
SimpleModel(just_subclasses=Foo(name="foo"))
SimpleModel(just_subclasses=Bar(description="desc"))

try:
    SimpleModel(just_subclasses=Other(etc="etc"))
except ValidationError as e:
    print(e)