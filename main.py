# BANK MANAGEMENT SYSTEM
import mysql.connector as con
import random

print('\t---WELCOME TO BANK MANAGEMENT SYSTEM---\n')


# ======================= USER FUNCTIONS =======================

def view_data():
    dbo = con.connect(host='localhost', user='root', password='password', database="bank_management_system")
    cu = dbo.cursor()
    number = int(input('Enter the account number: '))
    query = "SELECT * FROM acct_holder WHERE acc_no=%s"
    cu.execute(query, (number,))
    data = cu.fetchone()
    if data:
        print('Account number:', data[0])
        print('Name of account holder:', data[1])
        print('Phone number:', data[2])
        print("Email:", data[3])
        print("Address:", data[4])
        print('Initial balance:', data[5])
        print('Loan Taken:', data[6])
    else:
        print("No account found.")

    n = int(input('\nenter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


def update_name():
    dbo = con.connect(host='localhost', user="root", password='password', database='bank_management_system')
    cu = dbo.cursor()
    holder = input('Enter the updated name: ')
    number = int(input('Enter the account number: '))
    query = "UPDATE acct_holder SET acct_holder_name=%s WHERE acc_no=%s"
    cu.execute(query, (holder, number))
    dbo.commit()
    print('Name successfully updated')
    n = int(input('enter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


def update_email():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    email = input("Enter the updated email: ")
    number = int(input("Enter the account number: "))
    query = "UPDATE acct_holder SET email=%s WHERE acc_no=%s"
    cu.execute(query, (email, number))
    dbo.commit()
    print("Email updated successfully")
    n = int(input('enter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


def update_phone_number():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    phone = input("Enter the updated phone number: ")
    number = int(input("Enter the account number: "))
    query = "UPDATE acct_holder SET phone_number=%s WHERE acc_no=%s"
    cu.execute(query, (phone, number))
    dbo.commit()
    print("Phone number updated successfully")
    n = int(input('enter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


def update_address():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    address = input("Enter the updated address: ")
    number = int(input("Enter the account number: "))
    query = "UPDATE acct_holder SET address=%s WHERE acc_no=%s"
    cu.execute(query, (address, number))
    dbo.commit()
    print("Address updated successfully")
    n = int(input('enter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


def give_feedback():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    number = int(input("Enter your account number: "))
    feed = input("Enter your feedback:\n")
    query = "INSERT INTO feedback (feedback_text, acc_no) VALUES (%s, %s)"
    cu.execute(query, (feed, number))
    dbo.commit()
    print("Thank you for your feedback!")
    n = int(input('enter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


def view_loan_status():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    number = int(input("Enter your account number: "))
    query = "SELECT * FROM loan_acct WHERE acct_no=%s"
    cu.execute(query, (number,))
    data = cu.fetchone()
    if data:
        print("Account number:", data[0])
        print("Name:", data[1])
        print("Loan Amount:", data[2])
        print("Type of Loan:", data[3])
        print("Status:", data[4])
        print("Months unpaid:", data[5])
    else:
        print("No loan data found.")
    n = int(input('enter 1 for user menu:\nenter 2 for exit: '))
    if n == 1:
        user1()


# ======================= ADMIN FUNCTIONS =======================

def add_data():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()

    name = input("Enter the name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    balance = int(input("Enter balance: "))
    loan = input("Loan taken (yes/no): ")
    username = input("Create login username for this user: ")
    password = input("Create login password for this user: ")

    query1 = """
    INSERT INTO acct_holder
    (acct_holder_name, phone_number, email, address, initial_balance, loan_taken)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cu.execute(query1, (name, phone, email, address, balance, loan))
    dbo.commit()

    # Get the newly generated account number
    acc_no = cu.lastrowid

    query2 = "INSERT INTO user_data (username, password, acc_no) VALUES (%s, %s, %s)"
    cu.execute(query2, (username, password, acc_no))

    dbo.commit()

    print("New account added successfully")
    print(f"\tYour Account Number is: {acc_no}")
    print(f"\tUser Login Created → Username: {username}")


def view_loan_details():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    cu.execute("SELECT * FROM loan_acct")
    rows = cu.fetchall()
    for data in rows:
        print("Account number:", data[0])
        print("Name:", data[1])
        print("Loan Amount:", data[2])
        print("Type of Loan:", data[3])
        print("Status:", data[4])
        print("Months unpaid:", data[5])
        print("-------------------------")


def update_status_loan():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    number = int(input("Enter account number: "))
    stat = input("Enter loan status (cleared/pending): ")
    query = "UPDATE loan_acct SET status_of_loan=%s WHERE acct_no=%s"
    cu.execute(query, (stat, number))
    dbo.commit()
    print("Loan status updated!")


def status_loan_defaulters():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    m = int(input("Enter minimum months unpaid: "))
    query = "SELECT * FROM loan_acct WHERE number_of_months_from_which_interest_is_not_paid >= %s"
    cu.execute(query, (m,))
    rows = cu.fetchall()
    for data in rows:
        print("Account number:", data[0])
        print("Name:", data[1])
        print("Loan Amount:", data[2])
        print("Type of Loan:", data[3])
        print("Status:", data[4])
        print("Months unpaid:", data[5])
        print("-------------------------")


def add_data_loan():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    a = int(input("Enter account number: "))
    n = input("Enter name: ")
    p = int(input("Enter loan amount: "))
    e = input("Enter type of loan: ")
    ad = input("Enter status of loan: ")
    b = int(input("Enter months unpaid: "))
    query = "INSERT INTO loan_acct VALUES (%s, %s, %s, %s, %s, %s)"
    cu.execute(query, (a, n, p, e, ad, b))
    dbo.commit()
    print("Loan data added successfully")


def view_feedback():
    dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
    cu = dbo.cursor()
    cu.execute("SELECT * FROM feedback")
    rows = cu.fetchall()
    for data in rows:
        print("Feedback:", data[0])
        print("Account number:", data[1])
        print("-------------------------")


# ======================= MENUS =======================

def admin():
    while True:
        print("*WELCOME ADMIN*")
        print("1. Add new account")
        print("2. View loan details")
        print("3. Update loan status")
        print("4. View loan defaulters")
        print("5. View feedback")
        print("6. Add new loan account")
        print("7. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            add_data()
        elif ch == 2:
            view_loan_details()
        elif ch == 3:
            update_status_loan()
        elif ch == 4:
            status_loan_defaulters()
        elif ch == 5:
            view_feedback()
        elif ch == 6:
            add_data_loan()
        else:
            break


def user1():
    print("\t*WELCOME USER*")
    print("1. View account data")
    print("2. Update name")
    print("3. Update email")
    print("4. Update phone number")
    print("5. Update address")
    print("6. Give feedback")
    print("7. View loan status")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        view_data()
    elif ch == 2:
        update_name()
    elif ch == 3:
        update_email()
    elif ch == 4:
        update_phone_number()
    elif ch == 5:
        update_address()
    elif ch == 6:
        give_feedback()
    elif ch == 7:
        view_loan_status()


# ======================= MAIN MENU =======================

while True:
    print("***MAIN MENU***")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    inp = int(input("Enter your choice: "))

    if inp == 1:
        user = input("Enter username: ")
        pasw = input("Enter password: ")
        dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
        cu = dbo.cursor()
        cu.execute("SELECT * FROM admin_data")
        for data in cu:
            if data[0] == user and data[1] == pasw:
                admin()
                break
        else:
            print("Invalid admin login")

    elif inp == 2:
        user = input("Enter username: ")
        pasw = input("Enter password: ")
        dbo = con.connect(host="localhost", user="root", password="password", database="bank_management_system")
        cu = dbo.cursor()
        cu.execute("SELECT * FROM user_data")
        for data in cu:
            if data[0] == user and data[1] == pasw:
                user1()
                break
        else:
            print("Invalid user login")

    elif inp == 3:
        print("Thank you for using the Bank Management System!")
        break

