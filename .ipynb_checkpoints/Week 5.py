# # FOR loop= to iterate;iterable. the code always run from top to buttom.its either u set a range or its iterable
# # DRY
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# for num in range(6):
#     print(num+1) # since its index start from 0 not one, you can add 1 to print the entire number


# name = "mike"
# num = 481

# print(name.upper()) #method
# #print(num.upper())
# print(type(name)) #functiom
# print(type(num))
# for num in range(1,10): # end range is exclusive, start range is inclusive, which means it wont add d end number
#     print(num)
# for num in range(2,12):
#     print(num)
# for num in range(5,12,3): # 1(start range), 2(end range), 3(step), the 3 are optional only one is needed
#     print(num)
# for num in range(13,2, -1):
#     print(num)
# for num in range(4):
#     print(num)
#     print("yours")
#     print("please repeat me")
# print("it is mine")
# for num in range(3,37,3):
#     print(num)
# names_list = ["zaynab","Rahfah","Hiqmat","Aisha"]
# for name in names_list:
#     print(name)
# #OR
# print(names_list[0])
# print(names_list[1])
# print(names_list[2])
# print(names_list[3])
# list_length = len(names_list)
# print(list_length)
# for i in range(list_length):
#     print(i)
#     print(names_list[i])
# for i in range(list_length):
#     print(names_list[i])
#     if i == 2:
#         names_list[i] = "Faisolah"
#         print(names_list[i])
# names_list[i] = "Kenny"
# print(names_list[i])
# name = "Doctor kyle"

# for letter in name:
#     print(letter)
# for i in range(len(name)):
#     print(name[i])

# #WHILE loop: set an initial condition, or 

# counter = 1
# while counter < 10:
#     print("counting", counter)
#     counter +=1
#     if counter == 6:
#         break
# while counter < 15:
#     print("counting", counter)
#     counter +=1
#     if counter == 600:
#         break

    
#     LG_kwara = ["ilorin west","ekiti","oke-ero","ifelodun","barutee","asa"]
#     for i in LG_kwara:
#         print(i[-1])
# Use of length,split and replace
Country="Nigeria"
print(len("Country"))
for i in Country:
    print(i)
Sentence = "Nigeria is my country"
you = Sentence.split()
print(you)
My=Sentence.replace("my","our")
print(My)