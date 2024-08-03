
"""
Write a program to print the following star pattern.
          *
        * * *
      * * * * *           for n = 3
"""
n=3
for i in range(n+1):
    print(" "*(n-i),end="")           #print spaces
    print("*"*(2*i-1),end="")             #print * 2 times of multiple-1
    print("")                       #new line addition
