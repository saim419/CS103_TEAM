import pytest
import sqlite3
from transaction import transactions

@pytest.fixture(scope="module")
def db():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_add_transaction(db):
    transaction = transactions(db)
    transaction.add_transaction(1, 10.0, "Restaurant", "2022-07-19", "Chipotle")
    result = transaction.get_all_transactions()
    assert len(result) == 1
    assert result[0][1] == 1
    assert result[0][2] == 10.0
    assert result[0][3] == "Restaurant"
    assert result[0][4] == "2022-07-19"
    assert result[0][5] == "Chipotle"

def test_get_transaction(db):
    transaction = transactions(db)
    transaction.add_transaction(2, 100.0, "Furniture", "2022-08-05", "Couch")
    result = transaction.get_transaction(2)
    assert result[1] == 2
    assert result[2] == 100.0
    assert result[3] == "Furniture"
    assert result[4] == "2022-08-05"
    assert result[5] == "Couch"

def test_get_all_transactions(db):
    transaction = transactions(db)
    transaction.add_transaction(3, 100.0, "Restaurant", "2022-09-09", "AK's")
    transaction.add_transaction(4, 50.0, "Transportation", "2022-09-09", "Bus fare")
    result = transaction.get_all_transactions()
    assert len(result) == 4

def test_update_transaction(db):
    transaction = transactions(db)
    transaction.add_transaction(5, 100.0, "Dinner", "2022-03-05", "AMC")
    transaction.update_transaction(5, amount=300.0, category="Entertainment")
    result = transaction.get_transaction(5)
    assert result[2] == 300.0
    assert result[3] == "Entertainment"

def test_delete_transaction(db):
    transaction = transactions(db)
    transaction.add_transaction(6, 100.0, "Entertainment", "2023-01-01", "Concert")
    transaction.delete_transaction(6)
    result = transaction.get_all_transactions()
    assert len(result) == 5