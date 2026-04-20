from pydantic import BaseModel
from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from database import Base


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

class UserTable(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    stripe_customer_id: Mapped[Optional[str]] = mapped_column(nullable=True)

class TransactionTable(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column()
    status: Mapped[str] = mapped_column(default="pending")