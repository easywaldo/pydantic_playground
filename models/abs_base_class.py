import abc
from pydantic import BaseModel

class FooBarModel(BaseModel, abc.ABC):
    a: str
    b: int
    
    @abc.abstractclassmethod
    def my_abs_method(self):
        pass

class MyFooBar(FooBarModel):
    def my_abs_method(self):
        print('my foobar model')
        
my_foo_bar_model = MyFooBar(a="easywaldo", b = 100)
print(my_foo_bar_model)
