from pydantic import BaseModel, validator


class Txn(BaseModel):
    user_id: int
    txn: bool
    amount: float

    @validator("user_id")
    def user_id_validator(cls, v):
        if v < 0:
            raise ValueError("user_id must be positive")
        return v

    @validator("amount")
    def amount_validator(cls, v):
        if v < 0:
            raise ValueError("amount must be positive")
        return v

    @validator("txn")
    def type_validator(cls, v):
        if v not in [True, False]:
            raise ValueError("type must be boolean")
        return v
