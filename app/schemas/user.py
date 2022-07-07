from common.util import is_email
from pydantic import BaseModel, validator


class User(BaseModel):
    first_name: str
    last_name: str
    email: str

    @validator("email")
    def email_validator(cls, v):
        if is_email(identifier=v):
            return v
        else:
            raise ValueError("Invalid email address.")

    @validator("first_name")
    def first_name_validator(cls, v):
        if len(v) > 3:
            return v
        else:
            raise ValueError("Invalid first name.")

    @validator("last_name")
    def last_name_validator(cls, v):
        if len(v) > 3:
            return v
        else:
            raise ValueError("Invalid last name.")
