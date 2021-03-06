from datetime import datetime
from random import randint

from pydantic import BaseModel, PrivateAttr

class TimeAwareModel(BaseModel):
    _processed_at: datetime = PrivateAttr(default_factory=datetime.now)
    _secret_value: str = PrivateAttr()
    
    def __init__(self, **date):
        super().__init__(**date)
        self._secret_value = randint(1, 5)
        
m = TimeAwareModel()
print(m._processed_at)

print(m._secret_value)