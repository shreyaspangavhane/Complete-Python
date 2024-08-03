"""
    Write a program to print the following star pattern: 
        *
        **
        *** 
    
    for n = 3
"""

num=int(input("enter the number: "))
for i in range(num+1):
    print("*"*(2*i-1),end="")
    print("")
