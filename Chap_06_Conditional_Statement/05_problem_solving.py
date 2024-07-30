# 1. Write a program to find the greatest of four numbers entered by the user.
a1=int(input("Enter the 1st number: "))
a2=int(input("Enter the 2nd number: "))
a3=int(input("Enter the 3rd number: "))
a4=int(input("Enter the 4th number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print(a1 ,"is greater")

elif(a2>a1 and a2>a3 and a2>a4):
    print(a2 ,"is greater")

elif(a3>a2 and a3>a1 and a3>a4):
    print(a3 ,"is greater")

else:
    print(a4 ,"is greater")



# 2. Write a program to find out whether a student has passed or failed if it requires total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1=int(input("Enter ur marks: "))
marks2=int(input("Enter ur marks: "))
marks3=int(input("Enter ur marks: "))

total_percent=(100*(marks1+marks2+marks3))/300

if(total_percent>=40 and marks1>33 and marks2>33 and marks3>33):
    print("U are Passed!! ",total_percent)

else:
    print("Ur Fail ",total_percent)



#Q.3 A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

w1="Make a lot of money"
w2="buy now"
w3="subscribe this"
w4="click this"

message=input("enter ur message: ")
if((w1 in message) or(w2 in message) or(w3 in message) or(w4 in message)):
    print("detect these spams Message")
else:
    print("It's not spam")



# Q.4 Write a program to find whether a given username contains less than 10 characters or not
username=input("enter the username: ")
a=len(username)

if(a>10):
    print("Contain more than equal 10 letter")
else:
    print("Less than 10 number")


# Q.5 Write a program which finds out whether a given name is present in a list or not.
l1=["tony","stark","iron man","stark industries"]

user=input("enter the name: ")

if(user in l1):
    print("present")
else:
    print("not present")


"""Q.6 Write a program to calculate the grade of a student from his marks from the following scheme:
90 -100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
"""

grade=int(input("enter ur grade: "))
if( grade >90 and grade< 100):
    print("Ex")
    
elif( grade >80 and grade< 90):
    print("A")

elif( grade >70 and grade< 80):
    print("B")

elif( grade >60 and grade< 70):
    print("C")

elif( grade >50 and grade< 60):
    print("D")
    
else:
    print("F")



# 7.Write a program to find out whether a given post is talking about “Tony Stark” or not.


w1="Tony Stark is the actor name in movie.Tony Stark has work in marvel.Tony Stark is a iron man"

if("Tony Stark" in w1):
    print("This is taking about Tony Stark")
else:
    print("This is not taking about Tony Stark")


