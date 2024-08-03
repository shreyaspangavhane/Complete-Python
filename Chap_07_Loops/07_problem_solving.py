# 1. Write a program to print multiplication table of a given number using for loop.
num=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} * {i} = {i*num}")



"""
2.Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
"""
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    print(f"Hello, {i}")



# 3. Write a program to print multiplication table of a given number using while loop.
num=int(input("Enter the number: "))
i=1
while(i<11):
    print(f"{num} * {i} = {i*num}")
    i+=1



# 4.Write a program to find whether a given number is prime or not.
        #the number is not divisible by anothe rno. called prime

num=int(input("Enter the number: "))
for i in range(2,num):
    if(num%i==0):
        print("Number is Not Prime")
        break
    else:
        print("Number is Prime")
        break



# 5. Write a program to find the sum of first n natural numbers using while loop.
num=int(input("Enter the nth natural number: "))
i=1
sum=0
while(i<num):
    sum+=i
    i+=1
print(sum)



# 6.Write a program to calculate the factorial of a given number using for loop.
        # 5!=  1 X 2 X 3 X 4 X 5

num=int(input("Enter the number for factorial: "))
fact=1
for i in range(1,num+1):
    fact*=i

print(fact)


# 7. Write a program to print multiplication table of n using for loops in reversed
num=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} * {11-i} = {(11-i)*num}")

