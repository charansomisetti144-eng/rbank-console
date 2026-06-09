#=========================================================================================
# RBank - A simple banking system in Python
#=========================================================================================
#=========================================================================================
# Importing necessary libraries
#=========================================================================================
import os
from datetime import datetime
import random
import time
#=========================================================================================
# Global variables
#=========================================================================================
employee_id = "EMP001" 
employee_password = "admin123"
manager_id = "MGR001"
manager_password = "manager123"
customers = []
customers.append({
    "acc_no": 582741,
    "name": "Cherry",
    "age": 18,
    "mobile": "9876543210",
    "pin": "2008",
    "balance": 5000,
    "transactions": []
    
})

customers.append({
    "acc_no": 714258,
    "name": "Ravi",
    "age": 22,
    "mobile": "9876543211",
    "pin": "1234",
    "balance": 3000,
    "transactions": []
})
#=========================================================================================
# formatting functions
# =========================================================================================
def header(title):
    print("=" * 70)
    print(f"{title:^70}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S'):>70}")
    print("=" * 70)
    
def clear():
    os.system("cls")
def pause():
    input("Press Enter to continue...")
import time
import os

def welcome_screen():
    os.system("cls")

    welcome_text = "W  E  L  C  O  M  E     T  O"

    print("\n" * 2)

    for char in f"{welcome_text:^70}":
        print(char, end="", flush=True)
        time.sleep(0.05)

    time.sleep(1)

    print("\n\n")

    banner = [
        "██████╗ ██████╗  █████╗ ███╗   ██╗██╗  ██╗",
        "██╔══██╗██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝",
        "██████╔╝██████╔╝███████║██╔██╗ ██║█████╔╝",
        "██╔══██╗██╔══██╗██╔══██║██║╚██╗██║██╔═██╗",
        "██║  ██║██████╔╝██║  ██║██║ ╚████║██║  ██╗",
        "╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝"
    ]

    for line in banner:

        for char in f"{line:^70}":
            print(char, end="", flush=True)
            time.sleep(0.02)

        print()
    

    print("\n")

    for char in f"{'Y o u r  T r u s t e d  B a n k i n g  P a r t n e r':^70}":
        print(char, end="", flush=True)
        time.sleep(0.03)

    print("\n")
    time.sleep(2)
    pause()
# =========================================================================================
# Login functions
# =========================================================================================  
def customer_login():
    clear()
    header("Customer Login")
    attempt = 3
    while attempt > 0:
        clear()
        header("Customer Login")
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")
        clear()
        header("Customer Login")
        found = False
        for customer in customers:
            if str(customer["acc_no"]) == acc_no and customer["pin"] == pin:
                found = True
                clear()
                header("Customer Login")
                print("Customer Login Successful.")
                pause() 
                customer_menu(customer)
                return
            
        if not found:
            attempt -= 1
            if attempt > 0:
                print(f"Invalid Credentials!\nAttempts left: {attempt}")
                pause()
    print("Account Locked. Maximum attempts reached.")
    print("Please wait for 30 seconds before trying again.")
    time.sleep(30)
    print("You may try logging in again.")
    pause()

def employee_login():
    clear()
    header("Employee Login")
    attempt = 3
    while attempt > 0:
        clear()
        header("Employee Login")
        emp_id = input("Enter employee ID: ")
        emp_password = input("Enter employee password: ")
        clear()
        header("Employee Login")
        if emp_id == employee_id and emp_password == employee_password:
            clear()
            header("Employee Login")
            print("Employee login successful.")
            pause()
            employee_menu()
            return
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Invalid Credentials!\nAttempts left: {attempt}")
                pause()
    print("Account Locked. Maximum attempts reached.")
    print("Please wait for 30 seconds before trying again.")
    time.sleep(30)
    print("You may try logging in again.")
    pause()
def manager_login():
    clear()
    header("Manager Login")
    attempt=3
    while attempt > 0:
        clear()
        header("Manager Login")
        mgr_id = input("Enter manager ID: ")
        mgr_password = input("Enter manager password: ")
        clear()
        header("Manager Login")
        if mgr_id == manager_id and mgr_password == manager_password:
            clear()
            header("Manager Login")
            print("Manager login successful.")
            pause()
            manager_menu()
            return
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Invalid Credentials!\nAttempts left: {attempt}")
                pause()
    print("Account Locked. Maximum attempts reached.")
    print("Please wait for 30 seconds before trying again.")
    time.sleep(30)
    print("You may try logging in again.")
    pause()
def calculators_and_tools():
    clear()
    header("Calculators & Tools")
    while True:
        clear()
        header("Calculators & Tools")
        print("1. Interest Calculator")
        print("2. Age Calculator")
        print("3. Fixed Deposit Calculator")
        print("4. EMI Calculator")
        print("5. Loan Eligibility Calculator")
        print("6. Currency Converter")
        print("7. Recurring Deposit Calculator")
        print("8. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            interest_calculator()
        elif choice == "2":
            age_calculator()
        elif choice == "3":
            fixed_deposit_calculator()
        elif choice == "4":
            emi_calculator()
        elif choice == "5":
            loan_eligibility_calculator()
        elif choice == "6":
            currency_converter()
        elif choice == "7":
            recurring_deposit_calculator()
        elif choice == "8":
            break
        else:
            print("Invalid choice.")
            pause()
# =========================================================================================
# Menu functions
# =========================================================================================
def customer_menu(customer):

    while True:

        clear()
        header("Customer Menu")

        print("1. View Profile")
        print("2. Balance Inquiry")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Change PIN")
        print("7. Show Transaction History")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(customer)
        elif choice == "2":
            balance_enquiry(customer)
        elif choice == "3":
            deposit_money(customer)

        elif choice == "4":
            withdraw_money(customer)

        elif choice == "5":
            transfer_money(customer)

        elif choice == "6":
            change_pin(customer)
        elif choice == "7":
            show_transaction_history(customer)
        elif choice == "8":
            clear()
            for char in "Logging Out . . .":
                print(char, end="", flush=True)
                time.sleep(0.4)
            print() 
            break
        else:
            print("Invalid choice.")
            pause()
def employee_menu():
    while True:
        clear()
        header("Employee Menu")

        print("1. Create Customer Account")
        print("2. Search Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. View All Customers")
        print("6. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_customer()
        elif choice == "2":
            search_customer()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            view_all_customers()

        elif choice == "6":
            clear()
            for char in "Logging Out . . .":
                print(char, end="", flush=True)
                time.sleep(0.4)

            print() 
            break
        else:
            print("Invalid choice.")
            pause()
def manager_menu():
    clear()
    header("Manager Menu")
    while True:
        print("1. View Total Customers")
        print("2. View Total Bank Balance")
        print("3. View All Customers")
        print("4. View Highest Balance Customer")
        print("5. View Lowest Balance Customer")
        print("6. Search Customer")
        print("7. Bank Statistics")
        print("8. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            clear()
            header("Total Customers")
            print(f"Total number of customers: {len(customers)}")
            pause()
        elif choice == "2":
            clear()
            header("Total Bank Balance")
            total_balance = sum(customer["balance"] for customer in customers)
            print(f"Total bank balance: ₹{total_balance}")
            pause()
        elif choice == "3":
            view_all_customers()
        elif choice == "4":
            clear()
            header("Highest Balance Customer")
            if len(customers) == 0:
                print("No customers found.")
                pause()
                continue
            highest_balance_customer = max(customers, key=lambda x: x["balance"])
            print(f"Account Number : {highest_balance_customer['acc_no']}")
            print(f"Customer Name  : {highest_balance_customer['name']}")
            print(f"Age            : {highest_balance_customer['age']}")
            print(f"Mobile         : {highest_balance_customer['mobile']}")
            print(f"Balance        : ₹{highest_balance_customer['balance']}")
            pause()
        elif choice == "5":
            clear()
            header("Lowest Balance Customer")
            if len(customers) == 0:
                print("No customers found.")
                pause()
                continue
            lowest_balance_customer = min(customers, key=lambda x: x["balance"])
            print(f"Account Number : {lowest_balance_customer['acc_no']}")
            print(f"Customer Name  : {lowest_balance_customer['name']}")
            print(f"Age            : {lowest_balance_customer['age']}")
            print(f"Mobile         : {lowest_balance_customer['mobile']}")
            print(f"Balance        : ₹{lowest_balance_customer['balance']}")
            pause()
        elif choice == "6":
            search_customer()
        elif choice == "7":
            clear()
            header("Bank Statistics")
            total_customers = len(customers)
            total_balance = sum(customer["balance"] for customer in customers)
            average_balance = total_balance / total_customers if total_customers > 0 else 0
            print(f"Total Customers : {total_customers}")
            print(f"Total Bank Balance : ₹{total_balance}")
            print(f"Average Balance per Customer : ₹{average_balance:.2f}")
            pause()
        elif choice == "8":
            clear()
            for char in "Logging Out . . .":
                print(char, end="", flush=True)
                time.sleep(0.4)

            print() 
            break
        else:
            print("Invalid choice.")
            pause()
# ========================================================================================
# Random account number generator, PIN verification function and input validation functions
# ========================================================================================
def generate_account_number():
    while True:
        acc_no = random.randint(100000, 999999)

        exists = False

        for customer in customers:
            if customer["acc_no"] == acc_no:
                exists = True
                break

        if not exists:
            return acc_no
def verify_pin(customer):

    pin = input("Enter Your PIN : ")

    if pin == customer["pin"]:
        return True

    print("Incorrect PIN.")
    pause()
    return False
def get_positive_float(message):

    while True:

        value = input(message)

        if value.replace(".", "", 1).isdigit():

            value = float(value)

            if value > 0:
                return value

        print("Invalid Input")
# =========================================================================================
# employee operations
# =========================================================================================
#----------------Create Customer Account----------------
def create_customer():
    clear()
    header("Create Customer Account")

    acc_no = generate_account_number()

    # Name Validation
    while True:
        name = input("Enter Customer Name : ").strip()

        if not name:
            print("Customer name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Customer name should contain only letters.")
            continue

        break

    # Age Validation
    while True:
        age = input("Enter Age : ")

        if not age.isdigit():
            print("Age must contain only numbers.")
            continue

        age = int(age)

        if age < 18:
            print("Customer must be 18 years or older.")
            continue

        break

    # Mobile Validation
    while True:
        mobile = input("Enter Mobile Number : ")

        if not mobile.isdigit():
            print("Mobile number must contain only digits.")
            continue

        if len(mobile) != 10:
            print("Mobile number must contain exactly 10 digits.")
            continue

        break

    # PIN Validation
    while True:
        pin = input("Enter PIN : ")

        if not pin.isdigit():
            print("PIN must contain only digits.")
            continue

        if len(pin) != 4:
            print("PIN must contain exactly 4 digits.")
            continue

        confirm_pin = input("Confirm PIN : ")

        if pin != confirm_pin:
            print("PIN and Confirm PIN do not match.")
            continue

        break

    # Deposit Validation
    while True:
        deposit = input("Enter Initial Deposit : ")

        if not deposit.isdigit():
            print("Deposit must contain only numbers.")
            continue

        deposit = int(deposit)

        if deposit <= 0:
            print("Deposit amount must be greater than 0.")
            continue

        break

    customers.append({
        "acc_no": acc_no,
        "name": name,
        "age": age,
        "mobile": mobile,
        "pin": pin,
        "balance": deposit,
        "transactions": []
        
    })

    clear()
    header("ACCOUNT CREATED SUCCESSFULLY")

    print(f"Account Number : {acc_no}")
    print(f"Customer Name  : {name}")
    print(f"Balance        : ₹{deposit}")

    pause()
#----------------View All Customers----------------   
def view_all_customers():
    clear()
    header("All Customers")
    if len(customers) == 0:
        print("No customers found.")
        pause()
        return
    for customer in customers:
        print(f"Account Number : {customer['acc_no']}")
        print(f"Customer Name  : {customer['name']}")
        print(f"Age            : {customer['age']}")
        print(f"Mobile         : {customer['mobile']}")
        print(f"Balance        : ₹{customer['balance']}")
        print(f"pin            : {customer['pin']}")
        print("-" * 70)
    pause()
def search_customer():
    clear()
    header("Search Customer")
    if len(customers) == 0:
        print("No customers found.")
        pause()
        return
    search_acc_no = input("Enter Account Number to search: ")
    found = False
    for customer in customers:
        if str(customer["acc_no"]) == search_acc_no:
            print(f"Account Number : {customer['acc_no']}")
            print(f"Customer Name  : {customer['name']}")
            print(f"Age            : {customer['age']}")
            print(f"Mobile         : {customer['mobile']}")
            print(f"Balance        : ₹{customer['balance']}")
            found = True
            break
    if not found:
        print("Customer not found.")
    pause()
#----------------Update Customer Information----------------   
def update_customer():
    clear()
    header("Update Customer")
    found = False
    if len(customers) == 0:
        print("No customers found.")
        pause()
        return
    update_acc_no = input("Enter Account Number to update: ")
    for customer in customers:
        if str(customer["acc_no"]) == update_acc_no:
            found = True
            clear()
            header("Update Customer Information")
            print(f"Current Name  : {customer['name']}")
            print(f"Current Age   : {customer['age']}")
            print(f"Current Mobile: {customer['mobile']}")
            
            new_name = input("Enter new name (leave blank to keep current): ").strip()

            if new_name:
                while not new_name.replace(" ", "").isalpha():
                    print("Invalid name. Name should contain only letters.")
                    new_name = input("Enter new name : ").strip()

                customer["name"] = new_name


            new_age = input("Enter new age (leave blank to keep current): ").strip()

            if new_age:
                while not (new_age.isdigit() and int(new_age) >= 18):
                    print("Invalid age. Age must be a number and at least 18.")
                    new_age = input("Enter new age : ").strip()

                customer["age"] = int(new_age)


            new_mobile = input("Enter new mobile number (leave blank to keep current): ").strip()

            if new_mobile:
                while not (new_mobile.isdigit() and len(new_mobile) == 10):
                    print("Invalid mobile number. Mobile number must contain exactly 10 digits.")
                    new_mobile = input("Enter new mobile number : ").strip()

                customer["mobile"] = new_mobile
            print("Customer information updated successfully.")
            print(f"Name    : {customer['name']}")
            print(f"Age     : {customer['age']}")
            print(f"Mobile  : {customer['mobile']}")
            pause()
            return
    if not found:    
        print("Customer not found.")
        pause()
#----------------Delete Customer Account----------------
def delete_customer():
    clear()
    header("Delete Customer")
    found = False
    if (len(customers) == 0):
        print("No customers found.")
        pause()
        return
    delete_acc_no = input("Enter Account Number to delete: ")
    for i, customer in enumerate(customers):
        if str(customer["acc_no"]) == delete_acc_no:
            found = True
            print("Customer found.")
            pause()
            clear()
            header("Delete Customer Account")
            print(f"Account Number : {customer['acc_no']}")
            print(f"Customer Name  : {customer['name']}")
            print(f"Age            : {customer['age']}")
            print(f"Mobile         : {customer['mobile']}")
            print(f"Balance        : ₹{customer['balance']}")
            confirm = input("Are you sure you want to delete this account? (yes/no): ").lower()
            if confirm in ['yes', 'y']:
                customers.pop(i)
                print("Customer account deleted successfully.")
            else:
                print("Customer account deletion cancelled.")
            pause()
            return
    if not found:
        print("Customer not found.")
        pause()
# =================================================================================
# Customer operations
# =================================================================================
#----------------View Customer Profile----------------
def view_profile(customer):
    clear()
    header("Customer Profile")
    if not verify_pin(customer):
        return
    clear()
    header("Customer Profile")
    print(f"Account Number : {customer['acc_no']}")
    print(f"Customer Name  : {customer['name']}")
    print(f"Age            : {customer['age']}")
    print(f"Mobile         : {customer['mobile']}")
    print(f"Balance        : ₹{customer['balance']}")
    print(f"Transaction History :")
    for transaction in customer["transactions"]:
        print(f"{transaction['date']} - {transaction['type']} : ₹{transaction['amount']}")
    pause()
#----------------Balance Enquiry----------------
def balance_enquiry(customer):
    clear()
    header("Balance Enquiry")
    if not verify_pin(customer):
        return
    clear()
    header("Balance Enquiry")
    print(f"Current Balance : ₹{customer['balance']}")

    pause()
#----------------Deposit Money----------------
def deposit_money(customer):
    clear()
    header("Deposit Money")
    if not verify_pin(customer):
        return
    clear()
    header("Deposit Money")
    amount = input("Enter amount to deposit: ")
    while not (amount.isdigit() and int(amount) > 0):
        print("Invalid amount. Please enter a positive number.")
        amount = input("Enter amount to deposit: ")
    amount = int(amount)
    customer["balance"] += amount
    customer["transactions"].append({
        "type": "Deposit",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"₹{amount} deposited successfully.")
    print(f"New Balance : ₹{customer['balance']}")
    pause()
#----------------Withdraw Money----------------
def withdraw_money(customer):
    clear()
    header("Withdraw Money")
    if not verify_pin(customer):
        return
    clear()
    header("Withdraw Money")
    amount = input("Enter amount to withdraw: ")
    while not (amount.isdigit() and int(amount) > 0):
        print("Invalid amount. Please enter a positive number.")
        amount = input("Enter amount to withdraw: ")
    amount = int(amount)
    if amount > customer["balance"]:
        print("Insufficient balance.")
        pause()
        return
    customer["balance"] -= amount
    customer["transactions"].append({
        "type": "Withdrawal",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"₹{amount} withdrawn successfully.")
    print(f"New Balance : ₹{customer['balance']}")
    pause()
#----------------Transfer Money----------------
def transfer_money(customer):
    clear()
    header("Transfer Money")
    if not verify_pin(customer):
        return
    clear()
    header("Transfer Money")
    recipient_acc_no = input("Enter recipient account number: ")
    recipient = None
    for cust in customers:
        if str(cust["acc_no"]) == recipient_acc_no:
            recipient = cust
            break
    if recipient is None:
        print("Recipient account not found.")
        pause()
        return
    if recipient["acc_no"] == customer["acc_no"]:
        print("You cannot transfer money to your own account.")
        pause()
        return
    amount = input("Enter amount to transfer: ")
    while not (amount.isdigit() and int(amount) > 0):
        print("Invalid amount. Please enter a positive number.")
        amount = input("Enter amount to transfer: ")
    amount = int(amount)
    if amount > customer["balance"]:
        print("Insufficient balance.")
        pause()
        return
    customer["balance"] -= amount
    recipient["balance"] += amount
    customer["transactions"].append({
        "type": f"Transfer to {recipient['acc_no']}",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"₹{amount} transferred successfully to {recipient['acc_no']}.")
    print(f"New Balance : ₹{customer['balance']}")
    pause()
#----------------Change PIN----------------
def change_pin(customer):
    clear()
    header("Change PIN")
    if not verify_pin(customer):
        return
    clear()
    header("Change PIN")
    current_pin = input("Enter current PIN: ")
    if current_pin != customer["pin"]:
        print("Incorrect current PIN.")
        pause()
        return
    new_pin = input("Enter new PIN: ")
    while not (new_pin.isdigit() and len(new_pin) == 4):
        print("Invalid PIN. PIN must contain exactly 4 digits.")
        new_pin = input("Enter new PIN: ")
    confirm_pin = input("Confirm new PIN: ")
    if new_pin != confirm_pin:
        print("PIN and Confirm PIN do not match.")
        pause()
        return
    customer["pin"] = new_pin
    print("PIN changed successfully.")
    pause()
#----------------Show Transaction History----------------
def show_transaction_history(customer):
    clear()
    header("Transaction History")
    if not verify_pin(customer):
        return
    clear()
    header("Transaction History")
    if len(customer["transactions"]) == 0:
        print("No transactions found.")
        pause()
        return
    print("-" * 70)
    for transaction in customer["transactions"]:
        print(f"{transaction['date']} - {transaction['type']} : ₹{transaction['amount']}")
    print("-" *70)
    pause()
# =========================================================================================
# Calculators and Tools operations
# =========================================================================================
def interest_calculator():
    clear()
    header("Interest Calculator")
    while True:
        clear()
        header("Interest Calculator")
        print("1. Simple Interest Calculator")
        print("2. Compound Interest Calculator")
        print("3. Back to Calculators Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            principal = get_positive_float("Enter principal amount: ")
            rate = get_positive_float("Enter annual interest rate (in %): ")
            time = get_positive_float("Enter time (in years): ")
            simple_interest = (principal * rate * time) / 100
            total_amount = principal + simple_interest
            clear()
            header("Simple Interest Calculator")
            print(f"Principal Amount : ₹{principal}")
            print(f"Annual Interest Rate : {rate}%")
            print(f"Time : {time} years")
            print(f"Simple Interest : ₹{simple_interest:.2f}")
            print(f"Total Amount after {time} years : ₹{total_amount:.2f}")
            pause()
        elif choice == "2":
            principal = get_positive_float("Enter principal amount: ")
            rate = get_positive_float("Enter annual interest rate (in %): ")
            time = get_positive_float("Enter time (in years): ")
            compound_interest = principal * ((1 + rate / 100) ** time - 1)
            total_amount = principal + compound_interest
            clear()
            header("Compound Interest Calculator")
            print(f"Principal Amount : ₹{principal}")
            print(f"Annual Interest Rate : {rate}%")
            print(f"Time : {time} years")
            print(f"Compound Interest : ₹{compound_interest:.2f}")
            print(f"Total Amount after {time} years : ₹{total_amount:.2f}")
            pause()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
            pause()
    pause()
def age_calculator():
    clear()
    header("Age Calculator")
    while True:
        year = input("Enter birth year (YYYY): ")
        if year.isdigit():
            year = int(year)
            if 1900 <= year <= datetime.now().year:
                break
        print("Invalid year. Please enter a valid birth year.")
    while True:
        month = input("Enter birth month (1-12): ")
        if month.isdigit():
            month = int(month)
            if 1 <= month <= 12:
                break
        print("Invalid month. Please enter a valid birth month.")
    while True:
        day = input("Enter birth day (1-31): ")
        if day.isdigit():
            day = int(day)
            if 1 <= day <= 31:
                break
        print("Invalid day. Please enter a valid birth day.")
    today = datetime.now()
    years = today.year - year
    if (today.month, today.day) < (month, day):
        years -= 1
    print(f"\nAge Details:")
    print(f"Birth Date: {day}/{month}/{year}")
    print(f"Current Date: {today.day}/{today.month}/{today.year}")
    print(f"Age: {years} years")
    print(f"Next Birthday: {day}/{month}/{today.year + (1 if (today.month, today.day) >= (month, day) else 0)}")
    print("-" * 40)
    pause()
def fixed_deposit_calculator():
    clear()
    header("Fixed Deposit Calculator")
    while True:
        clear()
        header("Fixed Deposit Calculator")
        print("1. Simple Interest Fixed Deposit Calculator")
        print("2. Compound Interest Fixed Deposit Calculator")
        print("3. Back to Calculators Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            principal = get_positive_float("Enter principal amount: ")
            rate = get_positive_float("Enter annual interest rate (in %): ")
            time = get_positive_float("Enter time (in years): ")
            simple_interest = (principal * rate * time) / 100
            total_amount = principal + simple_interest
            clear()
            header("Simple Interest Fixed Deposit Calculator")
            print(f"Principal Amount : ₹{principal}")
            print(f"Annual Interest Rate : {rate}%")
            print(f"Time : {time} years")
            print(f"Simple Interest : ₹{simple_interest:.2f}")
            print(f"Total Amount after {time} years : ₹{total_amount:.2f}")
            pause()
        elif choice == "2":
            principal = get_positive_float("Enter principal amount: ")
            rate = get_positive_float("Enter annual interest rate (in %): ")
            time = get_positive_float("Enter time (in years): ")
            compound_interest = principal * ((1 + rate / 100) ** time - 1)
            total_amount = principal + compound_interest
            clear()
            header("Compound Interest Fixed Deposit Calculator")
            print(f"Principal Amount : ₹{principal}")
            print(f"Annual Interest Rate : {rate}%")
            print(f"Time : {time} years")
            print(f"Compound Interest : ₹{compound_interest:.2f}")
            print(f"Total Amount after {time} years : ₹{total_amount:.2f}")
            pause()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
            pause()
def emi_calculator():

    while True:

        clear()
        header("EMI Calculator")

        print("1. Home Loan EMI Calculator")
        print("2. Personal Loan EMI Calculator")
        print("3. Car Loan EMI Calculator")
        print("4. Education Loan EMI Calculator")
        print("5. Back to Calculators Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            loan_name = "Home Loan"
            default_rate = 8.5

        elif choice == "2":
            loan_name = "Personal Loan"
            default_rate = 12.0

        elif choice == "3":
            loan_name = "Car Loan"
            default_rate = 9.0

        elif choice == "4":
            loan_name = "Education Loan"
            default_rate = 10.0

        elif choice == "5":
            break

        else:
            print("Invalid Choice.")
            pause()
            continue

        clear()
        header(f"{loan_name} EMI Calculator")

        principal = get_positive_float("Enter Loan Amount : ")

        print(f"Recommended Interest Rate : {default_rate}%")

        rate = get_positive_float(
            "Enter Annual Interest Rate (%) : "
        )

        years = get_positive_float(
            "Enter Loan Tenure (Years) : "
        )

        monthly_rate = rate / (12 * 100)

        months = years * 12

        emi = (
            principal * monthly_rate
            * ((1 + monthly_rate) ** months)
        ) / (
            ((1 + monthly_rate) ** months) - 1
        )

        total_payment = emi * months

        total_interest = total_payment - principal

        clear()
        header(f"{loan_name} EMI Result")

        print(f"Loan Type          : {loan_name}")
        print(f"Loan Amount        : ₹{principal:,.2f}")
        print(f"Interest Rate      : {rate}%")
        print(f"Loan Tenure        : {years} Years")

        print("\n" + "=" * 50)

        print(f"Monthly EMI        : ₹{emi:,.2f}")
        print(f"Total Interest     : ₹{total_interest:,.2f}")
        print(f"Total Payment      : ₹{total_payment:,.2f}")

        print("=" * 50)

        pause()
def loan_eligibility_calculator():

    while True:

        clear()
        header("Loan Eligibility Calculator")

        print("1. Home Loan")
        print("2. Personal Loan")
        print("3. Car Loan")
        print("4. Education Loan")
        print("5. Back")

        choice = input("Enter your choice : ")

        if choice == "1":

            multiplier = 240
            loan_name = "Home Loan"

        elif choice == "2":

            multiplier = 60
            loan_name = "Personal Loan"

        elif choice == "3":

            multiplier = 84
            loan_name = "Car Loan"

        elif choice == "4":

            multiplier = 120
            loan_name = "Education Loan"

        elif choice == "5":
            break

        else:
            print("Invalid Choice")
            pause()
            continue

        salary = get_positive_float("Enter Monthly Salary : ")
        expenses = get_positive_float("Enter Monthly Expenses : ")
        existing_emi = get_positive_float("Enter Existing EMI : ")

        available_emi = (salary * 0.5) - existing_emi

        if available_emi <= 0:
            print("You are not eligible for a loan.")
            pause()
            continue

        eligible_loan = available_emi * multiplier

        clear()
        header(f"{loan_name} Eligibility Result")

        print(f"Loan Type        : {loan_name}")
        print(f"Monthly Salary   : ₹{salary}")
        print(f"Monthly Expenses : ₹{expenses}")
        print(f"Existing EMI     : ₹{existing_emi}")
        print(f"Available EMI    : ₹{available_emi:.2f}")
        print(f"Eligible Loan    : ₹{eligible_loan:.2f}")

        pause()
def currency_converter():

    USD_RATE = 83.50
    EUR_RATE = 95.00
    GBP_RATE = 112.00

    while True:

        clear()
        header("Currency Converter")

        print("1. INR → USD")
        print("2. USD → INR")
        print("3. INR → EUR")
        print("4. EUR → INR")
        print("5. INR → GBP")
        print("6. GBP → INR")
        print("7. Back")

        choice = input("Enter your choice : ")

        if choice == "7":
            break

        amount = get_positive_float(
            "Enter Amount : "
        )

        clear()
        header("Conversion Result")

        if choice == "1":

            converted = amount / USD_RATE

            print(f"₹{amount:,.2f} = ${converted:,.2f}")

        elif choice == "2":

            converted = amount * USD_RATE

            print(f"${amount:,.2f} = ₹{converted:,.2f}")

        elif choice == "3":

            converted = amount / EUR_RATE

            print(f"₹{amount:,.2f} = €{converted:,.2f}")

        elif choice == "4":

            converted = amount * EUR_RATE

            print(f"€{amount:,.2f} = ₹{converted:,.2f}")

        elif choice == "5":

            converted = amount / GBP_RATE

            print(f"₹{amount:,.2f} = £{converted:,.2f}")

        elif choice == "6":

            converted = amount * GBP_RATE

            print(f"£{amount:,.2f} = ₹{converted:,.2f}")

        else:

            print("Invalid Choice")
            pause()
            continue

        pause()
        
def recurring_deposit_calculator():

    while True:

        clear()
        header("Recurring Deposit Calculator")

        print("1. Calculate RD")
        print("2. Back")

        choice = input("Enter your choice : ")

        if choice == "1":

            monthly_deposit = get_positive_float(
                "Enter Monthly Deposit Amount : "
            )

            rate = get_positive_float(
                "Enter Interest Rate (%) : "
            )

            years = get_positive_float(
                "Enter Time Period (Years) : "
            )

            months = int(years * 12)

            total_investment = monthly_deposit * months

            maturity_amount = (
                monthly_deposit
                * months
                * (1 + (rate / 100) * years / 2)
            )

            interest_earned = (
                maturity_amount - total_investment
            )

            clear()
            header("RD Result")

            print(f"Monthly Deposit   : ₹{monthly_deposit:,.2f}")
            print(f"Interest Rate     : {rate}%")
            print(f"Time Period       : {years} Years")

            print("\n" + "=" * 50)

            print(f"Total Investment  : ₹{total_investment:,.2f}")
            print(f"Interest Earned   : ₹{interest_earned:,.2f}")
            print(f"Maturity Amount   : ₹{maturity_amount:,.2f}")

            print("=" * 50)

            pause()

        elif choice == "2":
            break

        else:
            print("Invalid Choice")
            pause()
# =========================================================================================
# Main program
# =========================================================================================
welcome_screen()
while True:
    clear()
    clear()
    header("WELCOME TO RBANK")
    print(f"{'1. Customer Login':^70}")
    print(f"{'2. Employee Login':^70}")
    print(f"{'3. Manager Login':^68}")
    print(f"{'4. Calculators & Tools':^75}")
    print(f"{'5. Exit':^60}")
    print("=" * 70)

    choice = input("Enter your choice: ")

    if choice == '1':
        customer_login()

    elif choice == '2':
        employee_login()

    elif choice == '3':
        manager_login()
    elif choice == '4':
        calculators_and_tools()
        
    elif choice == '5':
        print("Thank you for using RBank.")
        break

    else:
        print("Invalid choice.")

        continue_choice = input(
            "Do you want to continue? (yes/no): "
        ).lower()

        if continue_choice not in ['yes', 'y']:
            print("Thank you for using RBank.")
            break