from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from connection import init_db
from api import transactions, categories, goals, budgets, budget_categories, auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
app = FastAPI()

app.openapi_schema = {
    "openapi": "3.0.0",
    "components": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    },
    "security": [{"BearerAuth": []}]
}

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router, prefix="/api/v1", tags=["Auth"])
app.include_router(transactions.router, prefix="/api/v1", tags=["Transactions"])
app.include_router(categories.router, prefix="/api/v1", tags=["Categories"])
app.include_router(budgets.router, prefix="/api/v1", tags=["Budgets"])
app.include_router(goals.router, prefix="/api/v1", tags=["Goals"])
app.include_router(budgets.router, prefix="/api/v1", tags=["Budgets"])
app.include_router(budget_categories.router, prefix="/api/v1", tags=["BudgetCategories"])
