from transaction import transactions
import sys



def quit():
    sys.exit()


def showCategories():
    print(transactions.selectColumn(3))

#def addCategory():

#def modifyCategory():
    

def showTransactions(transactions):
    ''' print the transaction items '''
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s"%('itemNum','amount','category','date', 'description'))
    print('-'*40)
    for item in transactions:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-30s %2d"%values)

def addTransaction(new):
    transactions.add(new)

def deleteTransaction(rowid):
    transactions.delete(rowid)

def summarizeTransactionsByDate():
    print(transactions.selectColumn(4))

def summarizeTransactionsByMonth():
    #print the first char in the date string for each transaction
    # which is presumably month/day/year (US date system, not international)
    print(transactions.selectColumn(4)[0,2])

def summarizeTransactionsByYear():
    #print the first char in the date string for each transaction
    #                       01  2 34  5 67
    # which is presumably month / day / year (US date system, not international)
    print(transactions.selectColumn(4)[6,8])

def summarizeTransactionsByCategory():
    print(transactions.selectColumn(3))

def print_this_menu():
    ''' print an explanation of how to use this command '''
    print('''usage:
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
            )


'''def process_args(arglist):
    
    transactionsList = transactions()
    if arglist==[]:
        print_this_menu()
    elif arglist[0]=="show":
        showTransactions(transactionsList.selectActive())
    elif arglist[0]=="showall":
        showTransactions(tansactions = transactionsList.selectAll())
    elif arglist[0]=="showcomplete":
        showTransactions(transactionsList.selectCompleted())
    elif arglist[0]=='add':
        if len(arglist)!=3:
            print_this_menu()
        else:
            transaction = {'title':arglist[1],'desc':arglist[2],'completed':0}
            transactionsList.add(transaction)
    elif arglist[0]=='complete':
        if len(arglist)!= 2:
            print_this_menu()
        else:
            transactionsList.setComplete(arglist[1])
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_this_menu()
        else:
            transactionsList.delete(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_this_menu()'''


'''def toplevel():
     #read the command args and process them
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_this_menu()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()'''
