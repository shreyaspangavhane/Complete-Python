#Dict is the key value pair
# Dictionaries are changeable   so it is mutable

"""
PROPERTIES OF DICTIONARIES
    1.It is unordered.
    2.It is mutable.
    3.It is indexed.
    4.Cannot contain duplicate keys.
"""

b={}        # Empty dict

a={
    "name":"Iron Man",
    "owner":"Stark Industries",
    "movie":["Iron Man 1","Iron Man 2","Iron Man 3"],       #list used in dictionary
    "income_in_cr":189              #int data type
}

print(a)
print(a["movie"])

# print(a["Stark Industries"])        #not allowed


print(type(a))          #check the type

#cal length

print(len(a))