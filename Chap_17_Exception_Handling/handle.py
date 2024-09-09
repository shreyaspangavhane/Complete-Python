## Exception Handling is like as execute the plan B if plan A is failed
x= input("Enter Number 1: ")
y= input("Enter Number 2: ")        

# z=int(x)/int(y)
# when we enter the y as 0 exception is occured
# so for that use try catch block

try:
    z=int(x)/int(y)

except Exception as ecp:
    print("Exception Occured ",ecp)     ## display what kind of exception occured 
    z=0         # hadle the excption by assign z=0
print("Division is: ",z)