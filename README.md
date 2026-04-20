# FinTech API Prototype
Pierwsza faza budowy systemu transakcyjnego w Pythonie.

## Technologie
* FastAPI
* Pydantic
* Uvicorn
* SQLAlchemy 2.0
* SQLite + aiosqlite

## Status
Zaimplementowano architekturę bazy danych. System korzysta z **asynchronicznego silnika SQLAlchemy** oraz modeli ORM (`UserTable`, `TransactionTable`). Baza danych została przeniesiona z pamięci RAM do trwałego pliku SQLite (`finance.db`).