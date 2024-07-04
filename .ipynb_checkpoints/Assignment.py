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



class Person:
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height = height
    def Normal (self):
        print(f"This is {self.name}. He is {self.age}yrs old, with a height of {self.height}cm")

class Lecturer(Person):
    def lecturer(self,course):
        self.course=course
        print(f"The name of my lecturer is {self.name}` with an age of {self.age}, with a height of {self.height}cm and he teaches me {self.course}")

class Student(Person):
    def student(self, department):
        self.department=department
        print(f"My name is {self.name}. I'm {self.age}yrs old with a height of {self.height}cm, and in {self.department} department")

person1 = Person("Treasure", 20, 158)
person2 = Lecturer("Dr L.B Amusa", 40, 170)
person3 = Student("Oyetoke", 25, 160)

person1.Normal()
person2.lecturer("STA432")
person3.student("Statistics")
