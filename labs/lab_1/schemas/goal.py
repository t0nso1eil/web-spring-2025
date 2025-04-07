from datetime import date, datetime
from decimal import Decimal
from sqlmodel import SQLModel


class GoalBase(SQLModel):
    title: str
    target_amount: Decimal
    current_amount: Decimal = 0
    due_date: date

class GoalCreate(GoalBase):
    pass

class GoalRead(GoalBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True