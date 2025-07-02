from pydantic import BaseModel

class Counter(BaseModel):
    value: int = 0