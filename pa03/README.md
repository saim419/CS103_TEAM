# CS103a Spring 22

# L20

This git repository is for sharing code developed in the course lessons.
Each Lesson will be a different branch with the name L??.
Not all lessons have branches.

'''
Saim Siddiqui 
I worked on writing the pytest codes and the transaction.py and tracker.py methods all together. I did most of the work. But I was unable to debug some of the pytest test_transaction.py problems resolved.
'''
'''(base) saimsiddiqui@Saims-MacBook-Pro lesson19 % pytest test_transaction.py

============================= test session starts ==============================
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/saimsiddiqui/Desktop/Test/cs103aspr23/lesson19
plugins: anyio-2.2.0
collected 5 items                                                              

test_transaction.py ..FFF                                                [100%]

=================================== FAILURES ===================================
__________________________ test_get_all_transactions ___________________________

db = <sqlite3.Connection object at 0x7f7b68d16210>

    def test_get_all_transactions(db):
        transaction = Transaction(db)
        transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
        transaction.add_transaction(2, 50.0, "Transportation", "2022-03-05", "Bus fare")
        result = transaction.get_all_transactions()
>       assert len(result) == 2
E       AssertionError: assert 4 == 2
E        +  where 4 = len([(1, 1, 100.0, 'Fruit', '2022-03-05', 'Lunch'), (2, 1, 100.0, 'Fruit', '2022-03-05', 'Lunch'), (3, 1, 100.0, 'Fruit', '2022-03-05', 'Lunch'), (4, 2, 50.0, 'Transportation', '2022-03-05', 'Bus fare')])

test_transaction.py:37: AssertionError
___________________________ test_update_transaction ____________________________

db = <sqlite3.Connection object at 0x7f7b68d16210>

    def test_update_transaction(db):
        transaction = Transaction(db)
        transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
>       transaction.update_transaction(1, amount=300.0, category="Entertainment")

test_transaction.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <transaction.Transaction object at 0x7f7b68d729d0>, item_number = 1
amount = 300.0, category = 'Entertainment', date = None, description = None

    def update_transaction(self, item_number=None, amount=None, category=None, date=None, description=None):
        """
        Updates a transaction in the transactions table with the given id and parameters.
        """
        updates = []
        if item_number is not None:
            updates.append('item_number = {}'.format(item_number))
        if amount is not None:
            updates.append('amount = {}'.format(amount))
        if category is not None:
            updates.append('category = "{}"'.format(category))
        if date is not None:
            updates.append('date = "{}"'.format(date))
        if description is not None:
            updates.append('description = "{}"'.format(description))
    
        if len(updates) == 0:
            return
    
>       query = 'UPDATE transactions SET {} WHERE id = {}'.format(', '.join(updates), transaction_id)
E       NameError: name 'transaction_id' is not defined

transaction.py:64: NameError
___________________________ test_delete_transaction ____________________________

db = <sqlite3.Connection object at 0x7f7b68d16210>

    def test_delete_transaction(db):
        transaction = Transaction(db)
        transaction.add_transaction(1, 100.0, "Fruit", "2022-03-05", "Lunch")
        transaction.delete_transaction(1)
        result = transaction.get_all_transactions()
>       assert len(result) == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = len([(4, 2, 50.0, 'Transportation', '2022-03-05', 'Bus fare')])

test_transaction.py:52: AssertionError
=========================== short test summary info ============================
FAILED test_transaction.py::test_get_all_transactions - AssertionError: asser...
FAILED test_transaction.py::test_update_transaction - NameError: name 'transa...
FAILED test_transaction.py::test_delete_transaction - AssertionError: assert ...
========================= 3 failed, 2 passed in 0.16s ==========================
'''
