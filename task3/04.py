'''


Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.

    Create an __init__ method with parameters: account_number, name, balance.
    Create a put_money() method which deposit money in and would raise an exception for a negative argument.
    Create a withdraw() method which withdraw money out and would raise an exception for a negative argument.
    Create an apply_bank_fees() method to apply the bank fees with a percentage of 5% of the balance amount, deduct the balance with the calculated fee.
    Create a display() method to display account details.

Try thinking about what properties should be of class and which should be of instances, which should be public and which should be private.

'''

class BankAccount:
    def __init__(self, accountNumber: int, name: str, balance: float) -> None:
        self.accountNumber = int(accountNumber)
        self.name = str(name)
        self.__balance = float(balance)
    
    def put_money(self, added_amount: float) -> None:
        if added_amount < 0:
            raise Exception('negative argument')
        self.__balance += added_amount
    
    def withdraw(self, withdrawal_amount: float) -> None:
        if withdrawal_amount < 0:
            raise Exception('negative argument')
        if withdrawal_amount > self.__balance:
            raise Exception('not enough balance')
        self.__balance -= withdrawal_amount
    
    def apply_bank_fees(self) -> None:
        self.__balance = self.__balance * 0.95
    
    def display(self) -> None:
        print(f'Account Number : {self.accountNumber}, Name: {self.name}, Balance: {self.__balance}')
        