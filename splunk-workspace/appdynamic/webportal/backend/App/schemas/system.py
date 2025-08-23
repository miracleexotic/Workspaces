from pydantic import BaseModel


class ServiceStatus(BaseModel):
    state: bool
