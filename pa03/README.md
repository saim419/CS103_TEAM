# CS103a Spring 22

# L20

This git repository is for sharing code developed in the course lessons.
Each Lesson will be a different branch with the name L??.
Not all lessons have branches.

'''
Saim Siddiqui 
I worked on writing the pytest codes and the transaction.py and tracker.py methods all together. I did most of the work. But I was unable to debug some of the pytest test_transaction.py problems resolved.
'''

'''
(base) saimsiddiqui@Saims-MacBook-Pro lesson19 % pylint transaction.py
************* Module transaction
transaction.py:10:0: C0301: Line too long (110/100) (line-too-long)
transaction.py:27:0: C0301: Line too long (114/100) (line-too-long)
transaction.py:45:0: C0301: Line too long (108/100) (line-too-long)
transaction.py:64:0: C0301: Line too long (101/100) (line-too-long)
transaction.py:82:0: C0305: Trailing newlines (trailing-newlines)
transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transaction.py:23:4: R0913: Too many arguments (6/5) (too-many-arguments)
transaction.py:39:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:45:4: R0913: Too many arguments (6/5) (too-many-arguments)
transaction.py:64:86: E0602: Undefined variable 'transaction_id' (undefined-variable)

------------------------------------------------------------------
Your code has been rated at 6.74/10 (previous run: 7.89/10, -1.15) 



'''
'''
(base) saimsiddiqui@Saims-MacBook-Pro lesson19 % pylint tracker.py
************* Module tracker
tracker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tracker.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:26:21: E1101: Instance of 'Transaction' has no 'get_categories' member (no-member)
tracker.py:33:12: E1101: Instance of 'Transaction' has no 'add_category' member (no-member)
tracker.py:38:12: E1101: Instance of 'Transaction' has no 'modify_category' member (no-member)
tracker.py:40:23: E1120: No value for argument 'transaction_id' in method call (no-value-for-parameter)
tracker.py:47:12: E1120: No value for argument 'description' in method call (no-value-for-parameter)
tracker.py:54:18: E1101: Instance of 'Transaction' has no 'summarize_by_date' member (no-member)
tracker.py:58:18: E1101: Instance of 'Transaction' has no 'summarize_by_month' member (no-member)
tracker.py:62:18: E1101: Instance of 'Transaction' has no 'summarize_by_year' member (no-member)
tracker.py:66:18: E1101: Instance of 'Transaction' has no 'summarize_by_category' member (no-member)
tracker.py:20:0: R0912: Too many branches (27/12) (too-many-branches)
tracker.py:2:0: C0411: standard import "import sys" should be placed before "from transaction import Transaction" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 2.34/10 (previous run: 1.59/10, +0.76)

'''
I added all of these methods in tracker.py
'''
(base) saimsiddiqui@Saims-MacBook-Pro lesson19 % python3 tracker.py

    0. quit
    1. show categories
    2. add category
    3. modify category
    4. show transactions
    5. add transaction
    6. delete transaction
    7. summarize transactions by date
    8. summarize transactions by month
    9. summarize transactions by year
    10. summarize transactions by category
    11. print this menu
    
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
