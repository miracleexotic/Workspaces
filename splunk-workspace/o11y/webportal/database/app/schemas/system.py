from pydantic import BaseModel, ConfigDict


class ServiceStatus(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    state: bool
