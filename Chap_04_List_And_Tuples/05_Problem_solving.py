# Q.1 Write a program to store seven fruits in a list entered by the user.
fruits=[]
for i in range(7):
    fruit=input("Enter the 7 fruit name: ")
    fruits.append(fruit)
print(fruits)


# Q.2 Write a program to accept marks of 6 students and display them in a sorted manner.
stud=[]
for i in range(6):
    marks=int(input("Enter the marks of stud: "))
    stud.append(marks)
stud.sort()
print(stud)


# 3.Check that a tuple type cannot be changed in python.
        #tuple is immutable so it can't changed


# 4.Write a program to sum a list with 4 numbers.
l1=[1,4,7,2]
print(sum(l1))

# 5.Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
 
