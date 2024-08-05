# function with argument

def fun(name,greet):
    print("Good Day",name)
    print(greet)

fun("Shreyas","Thank you")

fun("Tony Stark","Thank you")


#function with argument with return value
print(" ")

def fun(name,greet):
    print("Good Day",name)
    print(greet)
    return "Done!!"

a=fun("Shreyas","Thank you")
print(a)