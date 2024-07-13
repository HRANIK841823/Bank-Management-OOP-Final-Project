from abc import ABC
class User(ABC):
    Bank_account = {}
    account_number = 1000

    def __init__(self, name, email, address, account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.password = password
        User.account_number += 1
        self.account_number = f"{self.account_type}{User.account_number}"
        self.transaction_history = []
        self.loan_count = 0
        User.Bank_account[self.account_number] = self
    
    @staticmethod
    def user_login(acc_num, acc_pass):
        if acc_num in User.Bank_account and User.Bank_account[acc_num].password == acc_pass:
            print("\n\n")
            print(f"{acc_num} Successfully Logged In To Your Account")
            return True
        return False

    def check_balance(self):
        print(f"\n\n{self.name}, Your Account Balance is {self.balance}")

    def deposit_balance(self, amount):
        bank.balance+=amount
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"\n\n{amount} is deposited in Your Account")
        print(f"Your Account New Balance is {self.balance}")

    def withdraw_balance(self, amount):
        if amount>=bank.balance:
            print("Bank is Bankrupt")
        elif amount<=bank.balance and amount <= self.balance:   
                bank.balance-=amount        
                self.balance -= amount
                self.transaction_history.append(f"Withdrew {amount}")
                print(f"\n\n{amount} is withdrawn from Your Account")
                print(f"Your Account New Balance is {self.balance}")           
        else:
            print("Withdrawal amount exceeded")
            print(f"Your Account Balance is {self.balance}")
            print("Please Enter Valid Amount")

    def check_transaction_history(self):
        print(f"Transaction history for {self.name}:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        bank.exist_balance_in_bank=bank.balance-self.balance
        if self.loan_count < 2:
            if amount<=bank.exist_balance_in_bank:
               bank.balance-=amount
               self.balance += amount
               self.loan_count += 1
               self.transaction_history.append(f"Loan taken from bank ---> {amount}")
               print(f"\n\nLoan of {amount} is granted and added to Your Account")
               print(f"{self.name} your Account Balance is : {self.balance}")
            else:
                print("Bank Doesnot Have Enough Amount")
        else:
            print("Loan limit exceeded")
            

    def transfer_amount(self, target_account_num, amount):
         target_account = next((account for account in User.Bank_account.values() if account.account_number == target_account_num), None)
         if target_account:
            if amount <= self.balance:
               self.balance -= amount
               target_account.balance += amount
               self.transaction_history.append(f"Transferred {amount} to {target_account.name}")
               target_account.transaction_history.append(f"Received {amount} from {self.name}")
               print(f"{amount} is transferred to {target_account.name}")
            else:
               print("Amount exceeded!!!!")
               print(f"Your Account Balance is {self.balance}")
               print("Please Enter Valid Amount")
         else:
            print("Account does not exist")


class Bank(ABC):
    def __init__(self, name, admin_id, password) -> None:
        self.name = name
        self.admin_id = admin_id
        self.password = password
        self.balance=0
        self.exist_balance_in_bank=0
        self.accounts = []
        self.total_loan_amount = 0
        self.loan = True

    def create_an_account(self, user):
        self.accounts.append(user)
        print(f"\n\nSuccessfully Open Account in {bank.name}")
        print(f"Your Account Number is: {user.account_number}")

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                del User.Bank_account[account_number]
                print(f"\n\nAccount {account.name} deleted successfully")
                return
        print("\n\nAccount not found")

    def all_user_accounts_list(self):
        print(f"\n\n_________All accounts of {self.name} Users_____________")
        i = 1
        for ac in self.accounts:
            print(f"\n\t{i}. ---->Ac Holder  Name: {ac.name}")
            print(f"\nEmail : {ac.email}")
            print(f"Total Balance: {ac.balance} ")
            print(f"Account Number: {ac.account_number}")
            print(f"Account Type: {ac.account_type}")
            print(f"Ac Holder Password: {ac.password}")
            i+=1
        
    def check_total_balance(self):
        total_balance = bank.balance
        print(f"Total available balance in the bank: {total_balance}")

    def check_total_loan_amount(self):
        total_loan_amount = sum(account.loan_count * 5000 for account in self.accounts)
        print(f"Total loan amount: {total_loan_amount}")

    def loan_on_off(self):
        self.loan = not self.loan
        status = "on" if self.loan else "off"
        print(f"Loan feature is now {status}")

class Admin:
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone

    def create_an_account(self, bank, user):
        bank.create_an_account(user)

    def delete_account(self, bank, account_number):
        bank.delete_account(account_number)

    def all_user_accounts_list(self, bank):
        bank.all_user_accounts_list()

    def check_total_balance(self, bank):
        bank.check_total_balance()

    def check_total_loan_amount(self, bank):
        bank.check_total_loan_amount()

    def loan_on_off(self, bank):
        bank.loan_on_off()

bank = Bank("Krishi Bank", "admin", 12345)

def admin_menu():
    admin_id = input("Enter Your ID(admin): ")
    admin_password = int(input("Enter Password(12345): "))
    if admin_id.lower() == bank.admin_id.lower() and admin_password == bank.password:
        admin = Admin("Karim", "karim@gmail.com", 23467937)
        while True:
            print("\n\n\t__________________________________")
            print("\n\t_______Welcome to Admin Panel______")
            print(f"\n\t__________{bank.name}______________")
            print("\n\t__________________________________")
            print("\n1 ---> Create an account")
            print("2 ---> Delete any user account")
            print("3 ---> See all user accounts list")
            print("4 ---> Check the total available balance of the bank")
            print("5 ---> Check the total loan amount")
            print("6 ---> On or Off the loan feature of the bank")
            print("7 ---> Exit")
            choice = int(input("\n\nEnter Your Choice: "))
            if choice == 1:
                name = input("Enter New AC holder Name: ")
                email = input("Enter AC holder email: ")
                address = input("Enter AC holder address: ")
                account_type = input("Enter AC holder Account type (SV or CR): ")
                password = int(input("Enter AC holder Password in Integer: "))
                user = User(name, email, address, account_type, password)
                admin.create_an_account(bank, user)
            elif choice == 2:
                account_number = input("\n\nEnter account number to delete: ")
                admin.delete_account(bank, account_number)
            elif choice == 3:
                print("\n\n*******All User*********")
                bank.all_user_accounts_list()
            elif choice == 4:
                admin.check_total_balance(bank)
            elif choice == 5:
                admin.check_total_loan_amount(bank)
            elif choice == 6:
                admin.loan_on_off(bank)
            elif choice == 7:
                break
            else:
                print("Invalid Choice")
    else:
        print("\n\nPlease Try Again, wrong ID and Password!!!")

def user_menu(user):
    while True:
        print(f"\n\n\t_______Welcome to User Panel {user.name}______")
        print("1 ---> Check balance")
        print("2 ---> Deposit amount")
        print("3 ---> Withdraw amount")
        print("4 ---> Check transaction history")
        print("5 ---> Take a loan")
        print("6 ---> Transfer amount")
        print("7 ---> Exit")
        choice = int(input("\n\nEnter Your Choice: "))
        if choice == 1:
            user.check_balance()
        elif choice == 2:
            amount = float(input("\n\nEnter amount to deposit: "))
            user.deposit_balance(amount)
        elif choice == 3:
            amount = float(input("\n\nEnter amount to withdraw: "))
            user.withdraw_balance(amount)
        elif choice == 4:
            user.check_transaction_history()
        elif choice == 5:
            if bank.loan_on_off:
                amount = float(input("\n\nEnter loan amount: "))
                user.take_loan(amount)
            else:
                print("Loan feature is currently off")
        elif choice == 6:
            acc_number = input("\n\nEnter the account number for transfer Money: ")
            amount = float(input("Enter amount to transfer: "))
            user.transfer_amount(acc_number, amount)
        elif choice == 7:
            break
        else:
            print("Invalid Choice")

while True:
    print("\n********||||Welcome To Our Bank ||||********")
    print(f"\n\t__________{bank.name}______________")
    print("1 ---> Admin")
    print("2 ---> User")
    print("3 ---> Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        acc_num = input("Enter Your Account Number(Fomate:SV1001): ")
        acc_pass = int(input("Enter Your Account Password: "))
        if User.user_login(acc_num, acc_pass):
            for user in bank.accounts:
                if user.account_number == acc_num:
                    user_menu(user)
                    break
        else:
           print("Wrong Account Number and Password")

    elif choice == 3:
        break
    else:
        print("Invalid Input")

    