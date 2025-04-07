from sqlmodel import SQLModel


class CategoryBase(SQLModel):
    name: str
    is_income: bool

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

    class Config:
        orm_mode = True