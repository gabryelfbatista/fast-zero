from pydantic import BaseModel  # type: ignore


class Message(BaseModel):
    message: str
