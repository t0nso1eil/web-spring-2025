from datetime import datetime
from typing import Optional
from decimal import Decimal
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")
    amount: Decimal
    type: TransactionType
    description: Optional[str] = None
    date: datetime = Field(default_factory=datetime.utcnow)

    user: Optional["User"] = Relationship(back_populates="transactions")
    category: Optional["Category"] = Relationship(back_populates="transactions")