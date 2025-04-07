from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from connection import get_session
from models.goal import Goal
from schemas.goal import GoalRead, GoalCreate

router = APIRouter()

@router.post("/goals/", response_model=GoalRead)
def create_goal(goal: GoalCreate, db: Session = Depends(get_session)):
    db_goal = Goal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@router.get("/goals/", response_model=list[GoalRead])
def get_goals(db: Session = Depends(get_session)):
    return db.query(Goal).all()

@router.get("/goals/{goal_id}", response_model=GoalRead)
def get_goal(goal_id: int, db: Session = Depends(get_session)):
    goal = db.get(Goal, goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Not found")
    return goal

@router.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_session)):
    goal = db.get(Goal, goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(goal)
    db.commit()
    return {"ok": True}