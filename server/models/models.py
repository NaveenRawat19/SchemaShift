from pydantic import BaseModel, Field
from typing import Optional

class UserAuth(BaseModel):
    username: str = Field(..., description="The username of the user")
    password: str = Field(..., description="The password of the user")
    # kerberos_ticket: Optional[str] = Field(None, description="Kerberos ticket for authentication")

class User(BaseModel):
    name: str
    email: str
    dob: str
    phone: str
    height: float
    weight: float
    