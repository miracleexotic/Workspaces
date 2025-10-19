from typing import List
from pydantic import BaseModel, ConfigDict, RootModel


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    username: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False


class Users(RootModel):

    root: List[User]
