from datetime import datetime
from decimal import Decimal
from enum import Enum
from sqlmodel import SQLModel


class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionBase(SQLModel):
    amount: Decimal
    type: TransactionType
    description: str | None = None
    date: datetime
    category_id: int

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True