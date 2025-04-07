from datetime import date, datetime
from typing import List
from sqlmodel import SQLModel, Field
from schemas.category import CategoryRead


class BudgetBase(SQLModel):
    month: date

class BudgetCreate(BudgetBase):
    pass

class BudgetCategoryRead(SQLModel):
    category_id: int
    limit_amount: float
    category: CategoryRead

    class Config:
        orm_mode = True

class BudgetRead(BudgetBase):
    id: int
    user_id: int
    created_at: datetime
    categories: List[BudgetCategoryRead]

    class Config:
        orm_mode = True