import sqlite3

class Transaction:
    """
    A class that interacts with a SQLite database to add, update, delete, and retrieve transactions.
    """

    def __init__(self, db_file):
        """
        Initializes a connection to the SQLite database and creates a transactions table if it does not exist.
        """
        self.conn = sqlite3.connect(str(db_file))
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                item_number INTEGER,
                                amount REAL,
                                category TEXT,
                                date TEXT,
                                description TEXT)''')
        self.conn.commit()

    def add_transaction(self, item_number, amount, category, date, description):
        """
        Adds a transaction to the transactions table with the given parameters.
        """
        sql = "INSERT INTO transactions (item_number, amount, category, date, description) VALUES (?, ?, ?, ?, ?)"
        values = (item_number, amount, category, date, description)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_transaction(self, transaction_id):
        """
        Retrieves a transaction from the transactions table with the given id.
        """
        self.cursor.execute('''SELECT * FROM transactions WHERE id = ?''', (transaction_id,))
        return self.cursor.fetchone()

    def get_all_transactions(self):
        sql = "SELECT * FROM transactions"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


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

        query = 'UPDATE transactions SET {} WHERE id = {}'.format(', '.join(updates), transaction_id)
        self.cursor.execute(query)
        self.conn.commit()

    def delete_transaction(self, item_number):
        """Deletes a transaction with the given item_number from the database."""
        sql = "DELETE FROM transactions WHERE item_number = ?"
        values = (item_number,)
        self.cursor.execute(sql, values)
        self.conn.commit()


    def __del__(self):
        """
        Closes the connection to the SQLite database when the object is deleted.
        """
        self.conn.close()



