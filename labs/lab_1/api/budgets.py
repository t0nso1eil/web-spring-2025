from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from connection import get_session
from models.budget import Budget
from models.budget_category import BudgetCategory
from schemas.budget import BudgetRead, BudgetCreate

router = APIRouter()

@router.post("/budgets/", response_model=BudgetRead)
def create_budget(budget: BudgetCreate, session: Session = Depends(get_session)):
    db_budget = Budget(**budget.dict())
    session.add(db_budget)
    session.commit()
    session.refresh(db_budget)
    return db_budget

@router.get("/budgets/{budget_id}", response_model=BudgetRead)
def get_budget(budget_id: int, session: Session = Depends(get_session)):
    budget = session.exec(
        select(Budget).where(Budget.id == budget_id).options(joinedload(Budget.categories).joinedload(BudgetCategory.category))
    ).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

@router.get("/budgets/", response_model=list[BudgetRead])
def get_budgets(session: Session = Depends(get_session)):
    return session.exec(
        select(Budget).options(joinedload(Budget.categories).joinedload(BudgetCategory.category))
    ).all()

@router.delete("/budgets/{budget_id}")
def delete_budget(budget_id: int, session: Session = Depends(get_session)):
    budget = session.get(Budget, budget_id)
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    session.delete(budget)
    session.commit()
    return {"ok": True}