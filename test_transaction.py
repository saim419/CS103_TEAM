import pytest
import sqlite3
from transaction import Transaction

@pytest.fixture(scope="module")
def db():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_add_transaction(db):
    transaction = Transaction(db)
    transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
    result = transaction.get_all_transactions()
    assert len(result) == 1
    assert result[0][1] == 1
    assert result[0][2] == 100.0
    assert result[0][3] == "Fruit"
    assert result[0][4] == "2022-03-05"
    assert result[0][5] == "Lunch"

def test_get_transaction(db):
    transaction = Transaction(db)
    transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
    result = transaction.get_transaction(1)
    assert result[1] == 1
    assert result[2] == 100.0
    assert result[3] == "Fruit"
    assert result[4] == "2022-03-05"
    assert result[5] == "Lunch"

def test_get_all_transactions(db):
    transaction = Transaction(db)
    transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
    transaction.add_transaction(2, 50.0, "Transportation", "2022-03-05", "Bus fare")
    result = transaction.get_all_transactions()
    assert len(result) == 2

def test_update_transaction(db):
    transaction = Transaction(db)
    transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
    transaction.update_transaction(1, amount=300.0, category="Entertainment")
    result = transaction.get_transaction(1)
    assert result[2] == 300.0
    assert result[3] == "Entertainment"

def test_delete_transaction(db):
    transaction = Transaction(db)
    transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
    transaction.delete_transaction(1)
    result = transaction.get_all_transactions()
    assert len(result) == 0
