from pydantic import BaseModel
from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

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

class Order(BaseModel):
    id: Optional[int] = None
    user_id: int
    package_id: str
    iccid: Optional[str] = None
    stripe_payment_id: str
    status: str = "pending"

class UserTable(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    stripe_customer_id: Mapped[Optional[str]] = mapped_column(nullable=True)

    orders: Mapped[list["OrderTable"]] = relationship(back_populates="user")

    cart_items: Mapped[list["CartItemTable"]] = relationship(back_populates="user")

class TransactionTable(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column()
    status: Mapped[str] = mapped_column(default="pending")

class OrderTable(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) # Łączy z użytkownikiem
    
    package_id: Mapped[str] = mapped_column() # ID pakietu eSIM
    iccid: Mapped[Optional[str]] = mapped_column(nullable=True) # Numer karty po zakupie
    
    stripe_payment_id: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column(default="pending")
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user: Mapped["UserTable"] = relationship(back_populates="orders")

class ProductTable(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(default=0)

    cart_items: Mapped[list["CartItemTable"]] = relationship(back_populates="product")


class CartItemTable(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(default=1)

    user: Mapped["UserTable"] = relationship()
    product: Mapped["ProductTable"] = relationship(back_populates="cart_items")
