
class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_balance
def deposit(self,amount):
  if amount>0:
    self.__account_balance+= amount
    print("deposited ₹{}.New Balance:₹{}".format(amount self.__account_balance))
  else:
    print("invaild deposite amount.please deposite a positive amount.")
def withdraw(self,amount):
  if amount>0 and amount<=self.__account_balance:
    self.__account_balance-= amount
print("withdraw₹{}.NewBalance:₹{}".format(amount,self.__account_balance))
else:
 print("invaild withdrawl amount or insufficientbalance.")
def display_balance(self):
  print("Account balance for{}(Account#{}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
account= BankAccount(account_number="123456789",account_holder_name="ponmani",initial_balance=50000.0)  