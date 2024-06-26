
LG_kwara = ["ilorin west","ekiti","oke-ero","ifelodun","barutee","asa","ilorin south","kaiama","sare"]
# # #print local government in even position
def  double(x):
     print(x*2)


length = len(LG_kwara)
for i in range(length):
     print(LG_kwara[i])
for i in range(1,length,2):
    print(LG_kwara[i])
#Another way
for i in range(length):
     if (i+1) % 2 ==0:
          print(LG_kwara[i])

for i in range(length):
     if i % 2==1:
          print(LG_kwara[i])

#for odd position
for i in range(length):
     if i % 2 ==0:
          print(LG_kwara[i])
# Another way
for i in range(0,length,2):
     print(LG_kwara[i])
# state that start with vowels
vowels = "aeiou"
for i in range(length):
     if LG_kwara[i][0] in "aeiou":
            print(LG_kwara[i])
#Another way
for lg in LG_kwara:
     if lg[0] in vowels:
          print(lg)
          
# double(3)
# double(7)
# double(15)

# for i in range (length):
#      LG_kwara[i] = LG_kwara[i] + "state"
#      print(LG_kwara[i])


print(LG_kwara)

for i in range (length):
     LG_kwara[i] = LG_kwara[i]  + "LGA"
     print(LG_kwara[i])
print(LG_kwara)