from pydantic import BaseModel


class Event(BaseModel):
    note: str
