# Question 0: Class for Bank Account
"""
Design a Python class named `BankAccount` to represent bank accounts.

Theory:
A bank account typically includes attributes such as account number, balance, and account holder name.
The class should handle operations such as deposit, withdrawal, and transfer of funds between accounts.

Operations:
1. Deposit: Add funds to the account
2. Withdrawal: Subtract funds from the account
3. Transfer: Transfer funds from one account to another

Test Cases:
Test Case 1:
acc1 = BankAccount("ACC001", 1000, "John Doe", 0000)
acc2 = BankAccount("ACC002", 2000, "Jane Smith", 2000)
# acc2.__password = 1000 
# print(acc2.__password) not able to change the password
# print(acc2.getPassWord())
print(acc2.setPassWord(2000,1000))
print(acc2.getPassWord())
assert acc1.balance == 1000
assert acc2.balance == 2000
print(acc1.deposit(500, 0000))
print(acc2.withdrawal(100, 2000))
print(acc1.transfer(acc2, 200, 0000))
assert acc1.balance == 1300
assert acc2.balance == 2200
"""

class BankAccount:
    
    def __init__(self,accountNumber, balance, accountHolderName,password):
        self.accountNumber = accountNumber
        self.balance = balance
        self.accountHolderName = accountHolderName
        self.__password = password

    def __auth(self,password):
        return self.__password == password
    
    def getPassWord(self):
        return self.__password
    
    def setPassWord(self,oldPassword,newPassword):
        if self.__auth(oldPassword):
            self.__password = newPassword
            return f"successfully Password changed."
        else:
            return f"Invalid user or password."

    def deposit(self,amount,password):
        if self.__auth(password):  
            self.balance += amount
            return f"Your current balance is {self.balance}."
        return f"Invalid info."
        
    def withdrawal(self,amount,password):
        if self.__auth(password):
            
            if self.balance > amount:
                self.balance -= amount
                return f"Your current balance is {self.balance}."
            else:
                return f"Insufficient funds."
        return f"Invalid info."
        
        
    def transfer(self,recieverAccNo,amount,password):
        if self.__auth(password):
            
            if self.balance > amount:
                self.balance -= amount
                recieverAccNo.balance += amount
            return f"Transferred {amount} to {recieverAccNo.accountHolderName} and Your current balance of your account is {self.balance}."
    
        return f"Invalid info"
        
acc1 = BankAccount("ACC001", 1000, "John Doe", 0000)
acc2 = BankAccount("ACC002", 2000, "Jane Smith", 2000)
# acc2.__password = 1000 
# print(acc2.__password) not able to change the password
# print(acc2.getPassWord())
print(acc2.setPassWord(2000,1000))
print(acc2.getPassWord())
assert acc1.balance == 1000
assert acc2.balance == 2000
print(acc1.deposit(500, 0000))
print(acc2.withdrawal(100, 2000))
print(acc1.transfer(acc2, 200, 0000))
assert acc1.balance == 1300
assert acc2.balance == 2200