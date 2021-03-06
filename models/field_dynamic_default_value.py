from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class Model(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

m1 = Model()
m2 = Model()

print(f'{m1.uid} != {m2.uid}')

print(f'{m1.updated_at} != {m2.updated_at}')

assert m1.updated_at == m2.updated_at