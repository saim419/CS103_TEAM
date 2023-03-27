import sqlite3
import csv

from importlib_metadata import re


def toDict(t):
    ''' t is a tuple (rowid, itemNum, amount,category, date, description)'''
    print('t='+str(t))
    transaction = {'rowid':t[0], 'itemNum':t[1], 'amount':t[2], 'category':t[3], 'date':t[4], 'description':t[5]}
    return transaction

class transactions():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum int, amount int, category text, date text, description text,)''',())
        #create a separate categories table so categories can be added and modified
        #if a category for an item does not exist in the categories list, the added item should
        #be rejected
        self.runQuery('''CREATE TABLE IF NOT EXISTS categories
                    (id int, name text)''',())
                    
    
    def selectActive(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transaction where completed=0",())

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELEC T rowid,* from transaction",())

    def selectColumn(self, columnID):
        ''' return all of the values from a certain column of the table'''
        return self.runQuery("SELECT column{columnID}, * from transactions")

    def selectCompleted(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transaction where completed=1",())

    def add(self,item):
        ''' create a transaction item and add it to the transactions table '''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?)",(item['itemNum'],item['amount'],item['category'],item['date'],item['description']))
        #self.runQuery("Insert INTO categories VALUES(?,?)", item['id'], item['name']))
    
    def delete(self,rowid):
        ''' delete a transaction item '''
        return self.runQuery("DELETE FROM transaction WHERE rowid=(?)",(rowid,))

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))

    def runQuery(self,query,tuple, filename):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(filename)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

'''def __init__(self, filename):
    conn = sqlite3.connect(filename)

    c = conn.cursor()

    c.execute(''CREATE TABLE transactions (
    itemNum int,
    amount int,
    category varChar(255),
    date varChar(255),
    description varChar(255),
)'')

    conn.commit()
    conn.close()'''

