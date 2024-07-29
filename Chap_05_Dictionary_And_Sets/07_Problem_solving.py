# Q.1 Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dict={
    "yash":"success",
    "ganda":"bad",
    "navin":"new"
}
user=input("enter the word do you want the meaning: ")
print(dict[user])



# Q.2 Write a program to input eight numbers from the user and display all the unique numbers (once).

a=set()
for i in range(8):
    user=int(input("enter the number: "))
    a.add(user)
print(a)



# Q.3 Can we have a set with 18 (int) and '18' (str) as a value in it?
        #       ->>yes
a={18,"18"}
print(a,type(a))



""" Q.4 What will be the length of following set s: 
    s = set() 
    s.add(20) 
    s.add(20.0) 
    s.add('20') # length of s after these operations?
"""
#->3
s = set() 
s.add(20) 
s.add(20.0)         #this is not print
s.add('20')
print(len(s))


# Q.5 s = {} What is the type of 's'?
s = {}
print(type(s))          #dict


# Q.6 Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

s={}
for i in range(4):
    name=input("Enter the name: ")
    lang=input("Enter the Fav Lang ")
    s.update({name:lang})

print(s)


# Q.7 If the names of 2 friends are same; what will happen to the program in problem 6?
#   ->>  last updated value become the print



# Q.8 If the lang of 2 friends are same; what will happen to the program in problem 6?
#   ->>  print as it is 


# Q.9 Can you change the values inside a list which is contained in set S? 
#   s = {8, 7, 12, "Harry", [1,2]}

# error shows