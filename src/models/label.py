from pydantic import BaseModel


class Label(BaseModel):
    key: str
    value: str
