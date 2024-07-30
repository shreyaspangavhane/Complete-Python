age=int(input("Enter ur age: "))

#if statement 1:
if(age%2==0):
    print("Age is even")


#if statement 2:
if(age>=18):
    print("U r 18+")
    print("Good for you!! ")

elif(age<0):
    print("Enter proper age")

elif(age==0):
    print("U R enter 0 age enter proper age")

else:
    print("ur age is not 18+")


print("End")