from fastapi import FastAPI, HTTPException
from models import User, Transaction
from typing import List
from database import init_db
from contextlib import asynccontextmanager

users_db: dict[int, User] = {}
transactions_db: dict[int, Transaction] = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Log: Rozpoczynam inicjalizację bazy danych...")
    await init_db()
    print("Log: Baza danych gotowa, tabele sprawdzone/stworzone.")
    yield
    print("Log: Zamykanie aplikacji...")

app = FastAPI(
    title="FinTech API",
    lifespan=lifespan)

@app.post("/user")
def create_user(new_user: User):
    new_id = len(users_db) + 1
    new_user.id = new_id
    users_db[new_id] = new_user
    return new_user

@app.get("/user")
def get_users():
    return users_db

@app.post("/transaction")
def create_transaction(new_transaction: Transaction):
    if new_transaction.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found!")

    new_id = len(transactions_db) + 1
    new_transaction.id = new_id
    transactions_db[new_id] = new_transaction
    return new_transaction

@app.get("/transaction")
def get_transactions():
    return transactions_db