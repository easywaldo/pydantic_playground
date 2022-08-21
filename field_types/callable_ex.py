from typing import Callable
from pydantic import BaseModel

class Foo(BaseModel):
    callback: Callable[[int], int]
    
m = Foo(callback=lambda x: print(x * x))
print(m)
