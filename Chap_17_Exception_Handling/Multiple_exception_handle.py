x= input("Enter Number 1: ")
y= input("Enter Number 2: ")        


try:
    z=int(x)/int(y)
    a="hello" + 3   # raise exception

except ZeroDivisionError as ecp:
    print("Exception Occured:",ecp)     ## display what kind of exception occured 
    z=0         # hadle the excption by assign z=0

except TypeError as tp:
    print("Exception Occured:",tp)

print("Division is: ",z)