# Write a program using functions to find greatest of three numbers.

def greater(a,b,c):
    if(a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    
    else:
        return c
a=3
b=5
c=2

print(f"Greatest Number is {greater(a,b,c)}")




# Write a python program using function to convert Celsius to Fahrenheit.

def convert(c,f):
    f=((9*c)/5)+32
    return f

c=int(input("Enter the Temp in Celsius: "))
f=0
print(f"The Fahrenheit is {convert(c,f)}")




# How do you prevent a python print() function to print a new line at the end.

    #  ->> using at last  end=""
print("Shreyas ",end="")
print("Pangavhane")




# Write a recursive function to calculate the sum of first n natural numbers.
print("\n Sum Calculate")
def sum(n):
        if(n==1):
             return 1
        return n + sum(n-1)

n=int(input("Enter the Number: "))
print(f"Sum of natural {n} number is: {sum(n)} ")



"""
Write a python function to print first n lines of the following pattern:
        ***
        **                                  - for n = 3
        *
"""
print("\n pattern print ")
def printpattern(n):
    if(n==0):
        return
    print("*"*n)
    printpattern(n-1)

printpattern(4)



# Write a python function to remove a given word from a list ad strip it at the same time.

def listremove(l1,word):
    n=[]
    for i in l1:
        if not(i==word):
            n.append(i.strip(word))
    return n
l1=["Rohan","Shubham","an"]
print(listremove(l1,"an"))