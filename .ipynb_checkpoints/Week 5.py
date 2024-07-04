# # # FOR loop= to iterate;iterable. the code always run from top to buttom.its either u set a range or its iterable
# # # DRY
# # print(1)
# # print(2)
# # print(3)
# # print(4)
# # print(5)
# # print(6)
# # for num in range(6):
# #     print(num+1) # since its index start from 0 not one, you can add 1 to print the entire number


# # name = "mike"
# # num = 481

# # print(name.upper()) #method
# # #print(num.upper())
# # print(type(name)) #functiom
# # print(type(num))
# # for num in range(1,10): # end range is exclusive, start range is inclusive, which means it wont add d end number
# #     print(num)
# # for num in range(2,12):
# #     print(num)
# # for num in range(5,12,3): # 1(start range), 2(end range), 3(step), the 3 are optional only one is needed
# #     print(num)
# # for num in range(13,2, -1):
# #     print(num)
# # for num in range(4):
# #     print(num)
# #     print("yours")
# #     print("please repeat me")
# # print("it is mine")
# # for num in range(3,37,3):
# #     print(num)
# # names_list = ["zaynab","Rahfah","Hiqmat","Aisha"]
# # for name in names_list:
# #     print(name)
# # #OR
# # print(names_list[0])
# # print(names_list[1])
# # print(names_list[2])
# # print(names_list[3])
# # list_length = len(names_list)
# # print(list_length)
# # for i in range(list_length):
# #     print(i)
# #     print(names_list[i])
# # for i in range(list_length):
# #     print(names_list[i])
# #     if i == 2:
# #         names_list[i] = "Faisolah"
# #         print(names_list[i])
# # names_list[i] = "Kenny"
# # print(names_list[i])
# # name = "Doctor kyle"

# # for letter in name:
# #     print(letter)
# # for i in range(len(name)):
# #     print(name[i])

# # #WHILE loop: set an initial condition, or 

# # counter = 1
# # while counter < 10:
# #     print("counting", counter)
# #     counter +=1
# #     if counter == 6:
# #         break
# # while counter < 15:
# #     print("counting", counter)
# #     counter +=1
# #     if counter == 600:
# #         break

    
# #     LG_kwara = ["ilorin west","ekiti","oke-ero","ifelodun","barutee","asa"]
# #     for i in LG_kwara:
# #         print(i[-1])
# # Use of length,split and replace
# Country="Nigeria"
# print(len("Country"))
# for i in Country:
#     print(i)
# Sentence = "Nigeria is my country"
# you = Sentence.split()
# print(you)
# My=Sentence.replace("my","our")
# print(My)

# FUNCTIONS AND ARGUMENT
# def double(x):
#     print(x*2)
# double(2)
# def greeting():
#     print ("good morning oyetoke")
# greeting()
# #def power2():
# def greeting(name = "user"):
#     print ("good morning", name)
#     print("good morning"+ name)
#     print("good morning "+ name)
#     print("good morning "+ name)

# greeting()

# def greeting(country, name = "user"):
#     print ("good morning", name, ",How is", country)
#     print("good morning "+ name + " ,How is " + country)
#     print(f'good morning{name}, how is {country}')
# greeting("Texas", "Emma")

# def greeting(country, name = "user"):
#      print(f'good morning{name}, how is {country}')
#      return "we are done "
# greeting("USA")
# print()
# print(greeting("Canada", "Tosin"))
# print()
# a = greeting("Korea", " Kenny")

# print ("this is the result of greeting user",a)

# # print(2**5)
# def power(num, index):
#       print(num**index)

# var1 = 2
# var2 = 5

# power(var1, var2)
# #power(4,5)

# power(4,3)

# # Create a function that would calculate the Tax on a good
# #That would print every item on a list adding "s" to the front

# # def cal(Goods,Tax):
# #       print(Goods*Tax)
# # Tax=cal(2390,0.8 + VA)
# #correction on tax
# def Total_Price(amount, tax_percentage):
#       total = amount + (amount * tax_percentage/100)
#       print(total)
#       return(total)

# ans = Total_Price(1000,25)
# print(ans)
# print(ans + 2000)
# print(ans + 0.9)

# #2
# def PluraliseItems(ItemsList):
#       for Item in ItemsList:
#             print(Item + "s")
# Sample=["Car","Phone","Laptop","shoe"]
# PluraliseItems(Sample)

# def PluraliseItems(ItemsList):
#       for Item in ItemsList:
#             if Item [-1] == "e" and Item [-2] == "f":
#                   print(Item[0:-2] + "ves")
#                   continue
#             print(Item + "s")
# Samples=["Car", "Plate", "Phone", "Wife", "Knife"]
# PluraliseItems(Samples)

# amount = "2000"
# val = int(amount)
# print(val//3)
# print(val/3)

# amount = "2000N"
# amount = amount.strip("N")
# print(amount)
# val = int(amount)

# to seprate is split,strip(to remove a value in btw),join is to add back

# write a function that adds an argument to the end of a list

# list=["STA","MAT","CSC"]
# def my_list(list):
#     for items in list:
#         print(items)
# my_list(list)
# write a f(x) to change classes of the first element of ur list to ABU


# list = ["STA","MAT","CSC"]
# new_list = "zly"
# Newest= (list,new_list)
# print(Newest)

# 1st method, not modifying the content of the list

# def add_weights(weights):
#     total = 0
#     for weight in weights:
#         strval = weight.strip("kg")
#         numval = int(strval)
#         total = total + numval
#         #return total
#    return (total)

# next = ["2000kg","100kg","500kg"]
# ans = add_weights(next)
# print(ans)
# print("average is:", ans/3)
# print(f"average is:{ans/3}")



# numbers=[2,4,5,6,4,8]
# # def add_list(numbers):
# #     total = 0
# #     for i in numbers:
# #         total = total + numbers
# #         return total
# #     ans = add_list(list4)
# #     print(ans)
# # first way to add
# def totalsum(values):
#     total = 0
#     for val in values:
#         total = total + val
#     return total
# ans3 = totalsum(numbers)
# print(ans3)
# # 2nd way to add
# def totalsum2(values):
#     ans = sum(values)
#     return ans
# newans = totalsum2(numbers)
# print(newans)
# #3rd way to add
# anotherans = sum(numbers)
# print(anotherans)



# # Print("sample")
# my_list = [2, "good" ]
# our_list = [2,4,8]
# var = 4
# word = "good"
# print(type(our_list))
# print(type(my_list))
# my_list.append("new")
# print(my_list)
# print(type(var))
# print(type(word))
# print(type({}))

#CLASS: THIS IS A WAY TO CREATE UR OWN DATATYPE IN PYTHON
 #initialization method(function)(init) is like creating a template to get data from the class
# class Car:
#     def __init__(self, color,make,model):
#         self.color = color
#         self.b = make
#         self.c = model
#         # print("new instance of car created")
#     def describe(self):
#         print(f"this is a {self.color} {self.b} {self.c}")
# 
# # any code in the init part will automatically run
# print("new car created")

# car1 = Car("blue", "toyota","camry")
# car2 = Car("wine", "Benz","mercedes")
# vehicle3 = Car("grey", "Lexus", "jeep")   
# # the three codes are independent of each other
# print(car1.color)
# print(car2.color)
# print(vehicle3.c)
# car1.describe()
# vehicle3.describe()
# car2.describe
# print(vehicle3.color)
# car1.color = "green"
# car1.describe()
# car1.b = "venza"
# car1.describe()

class Animals:

    #age, weight, height, color
    def __init__(self, age,weight,height,color):
        self.age = age
        self.weight = weight
        self.height = height
        self.color = color

    def describe(self):
            print(f"This is a {self.color} {self.age}yrs old {self.weight} animal, with a height of {self.height}")
animal1 =Animals(5, "2kg", "15cm", "black")
animal1.describe()
animal1.age = 25
animal1.describe()



class Mammal(Animals):
    #  def describe(self):
     def describeMammal(self):        
            # print(f"This is a {self.color} {self.age}yrs old {self.weight} mammal, with a height of {self.height}")
             print(f"This is a {self.color} {self.age}yrs old {self.weight} mammal")
            
     pass  # you can use dis to inherit 
cat1 = Mammal(4, "2kg", "15cm", "blue")
cat1.describe()
cat1.describeMammal()

