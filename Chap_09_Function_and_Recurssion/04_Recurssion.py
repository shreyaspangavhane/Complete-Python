# Recurssion is the function which call itself

"""

factorial 4= 4 X 3 X 2 X 1 

factorial 1= 1 
factorial 2= 2 X 1 
factorial 3=  3 X 2 X 1 
factorial 4= 4 X 3 X 2 X 1 

factorial(n)=n*factorial(n-1)


"""

def factorial(n):
    if(n==1 or n==0):
        return 1
    
    return n*factorial(n-1)

n=int(input("Enter the Number: "))
print(f"Factorial of {n} is {factorial(n)}")