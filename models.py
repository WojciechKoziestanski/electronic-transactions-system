from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TransactionStatus(str, Enum):
    PENDING = "Pending"
    SUCCES = "Succes"
    FAILED = "Failed"

class User(BaseModel):
    id: Optional [int] = None
    email: str
    stripe_customer_id: Optional [str] = None

class Transaction(BaseModel):
    id: Optional [int] = None
    user_id: int
    amount: float
    status: TransactionStatus = TransactionStatus.PENDING