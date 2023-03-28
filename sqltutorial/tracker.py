from transaction import Transaction
import sys

def print_menu():
    print('''
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
    ''')

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction '''
    transaction = Transaction()
    if arglist == []:
        print_menu()
    elif arglist[0] == "show categories":
        categories = transaction.get_categories()
        for category in categories:
            print(category)
    elif arglist[0] == "add category":
        if len(arglist) != 2:
            print("Usage: add category <category>")
        else:
            transaction.add_category(arglist[1])
    elif arglist[0] == "modify category":
        if len(arglist) != 3:
            print("Usage: modify category <old_category> <new_category>")
        else:
            transaction.modify_category(arglist[1], arglist[2])
    elif arglist[0] == "show transactions":
        transactions = transaction.get_transactions()
        for transaction in transactions:
            print(transaction)
    elif arglist[0] == "add transaction":
        if len(arglist) != 5:
            print("Usage: add transaction <date> <category> <description> <amount>")
        else:
            transaction.add_transaction(arglist[1], arglist[2], arglist[3], arglist[4])
    elif arglist[0] == "delete transaction":
        if len(arglist) != 2:
            print("Usage: delete transaction <transaction_id>")
        else:
            transaction.delete_transaction(arglist[1])
    elif arglist[0] == "summarize transactions by date":
        summary = transaction.summarize_by_date()
        for date, total in summary.items():
            print(f"{date}: {total}")
    elif arglist[0] == "summarize transactions by month":
        summary = transaction.summarize_by_month()
        for month, total in summary.items():
            print(f"{month}: {total}")
    elif arglist[0] == "summarize transactions by year":
        summary = transaction.summarize_by_year()
        for year, total in summary.items():
            print(f"{year}: {total}")
    elif arglist[0] == "summarize transactions by category":
        summary = transaction.summarize_by_category()
        for category, total in summary.items():
            print(f"{category}: {total}")
    elif arglist[0] == "print this menu":
        print_menu()
    else:
        print(f"Error: {arglist[0]} is not a valid command")
        print_menu()

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, so prompt for them in a loop
        print_menu()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n
toplevel()