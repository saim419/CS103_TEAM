import sqlite3

class Transaction:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
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
        self.cursor.execute('''INSERT INTO transactions (item_number, amount, category, date, description)
                                VALUES (?, ?, ?, ?, ?)''', (item_number, amount, category, date, description))
        self.conn.commit()

    def get_transaction(self, id):
        self.cursor.execute('''SELECT * FROM transactions WHERE id = ?''', (id,))
        return self.cursor.fetchone()

    def get_all_transactions(self):
        self.cursor.execute('''SELECT * FROM transactions''')
        return self.cursor.fetchall()

    def update_transaction(self, id, item_number=None, amount=None, category=None, date=None, description=None):
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

        query = 'UPDATE transactions SET {} WHERE id = {}'.format(', '.join(updates), id)
        self.cursor.execute(query)
        self.conn.commit()

    def delete_transaction(self, id):
        self.cursor.execute('''DELETE FROM transactions WHERE id = ?''', (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
