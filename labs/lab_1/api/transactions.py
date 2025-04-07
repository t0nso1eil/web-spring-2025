from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from connection import get_session
from models.transaction import Transaction
from schemas.transaction import TransactionRead, TransactionCreate

router = APIRouter()

@router.post("/transactions/", response_model=TransactionRead)
def create_transaction(tr: TransactionCreate, db: Session = Depends(get_session)):
    db_tr = Transaction(**tr.dict())
    db.add(db_tr)
    db.commit()
    db.refresh(db_tr)
    return db_tr

@router.get("/transactions/", response_model=list[TransactionRead])
def get_transactions(db: Session = Depends(get_session)):
    return db.query(Transaction).all()

@router.get("/transactions/{transaction_id}", response_model=TransactionRead)
def get_transaction(transaction_id: int, db: Session = Depends(get_session)):
    tr = db.get(Transaction, transaction_id)
    if not tr:
        raise HTTPException(status_code=404, detail="Not found")
    return tr

@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_session)):
    tr = db.get(Transaction, transaction_id)
    if not tr:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(tr)
    db.commit()
    return {"ok": True}