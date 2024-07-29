# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

user=input("Enter the ur name: ")
print(f"Good Afternoon {user}")
# print("Good Afternoon",user)



#Q.2  Write a program to fill in a letter template given below with name and date. 
""" letter = ''' Dear <|Name|>, 
You are selected! 
<|Date|> ''' """

letter=letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>","Shreyas").replace("<|Date|>","28 Jun"))




# Q.3  Write a program to detect double space in a string.
name="Tony  Stark"
print(name.find("  "))



# Q.4 Replace the double space from problem 3 with single spaces.
name="Tony  Stark"
print(name.replace("  "," "))



# Q.5 Write a program to format the following letter using escape sequence characters. 
"""letter = "Dear Harry, this python course is nice. Thanks!" """ 
letter = "Dear Harry, \nthis python course is nice.\nThanks!"
print(letter)


