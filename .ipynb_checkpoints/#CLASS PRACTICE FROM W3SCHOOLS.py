#CLASS PRACTICE FROM W3SCHOOLS
# A class is like an object constructor, or a blueprint for creating objects.
# we use the keyword class to create a class
# create a class named My_studio, wih a property named x:
class My_studio:
    x = 5
print(My_studio)
#use the class named My_studio to create objects
ply = My_studio()
print(ply.x)
# The __init__()function
#it is always executed when the class is being initiated.
# We use it to assign values to object properties, or other operations that are necesaary to do when the object is being created
class Mine:
    def __init__(self, name, age):
        self.name = name
        self.age = age
attribute = Mine("Treasure", 20)

print(attribute.name)
print(attribute.age)


class BankAccount:

    def __init__(self, accname, accno, accbal):
        self.accname = accname
        self.accno = accno
        self.accbal = accbal

def deposit(self, amount):
     amount = 20000
     self.deposit = deposit+self.accbal
     return self.deposit
def withdrawal(self, withdraw):
    withdraw = 10000
    self.withdraw = self.deposit-withdraw
    return self.withdraw
def CheckBalance (self, balance):
    balance = self.withdraw
    return balance
account1=BankAccount("Oyetoke", 2220456789, 200000)
account2 = BankAccount("Treasure", 3245780198, 300000)
def descibe(self):
    print(f"After Depositing, My account {accname} with account no {accno}, has {accbal}")
    print(f"After withdrawing My account {accname} with account no {accno}, has {accbal}")
