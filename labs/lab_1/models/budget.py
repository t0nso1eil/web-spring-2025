from datetime import datetime, date
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Budget(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    month: date
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional["User"] = Relationship(back_populates="budgets")
    categories: List["BudgetCategory"] = Relationship(back_populates="budget")