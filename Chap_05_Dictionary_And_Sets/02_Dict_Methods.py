# Methods()

a={
    "name":"Iron Man",
    "owner":"Stark Industries",
    "movie":["Iron Man 1","Iron Man 2","Iron Man 3"],       #list used in dictionary
    "income_in_cr":189              #int data type
}

# a.items()  ->give value in form of key-value in tuple
print(a.items())


#a.key()     ->gives all the key
print(a.keys())


#a.value()     ->gives all the value
print(a.values())


#a.update("key":"value")    
a.update({"name":"Tony Stark","age":"48"})       #here age is not present so it add in dict
print(a)


#a.pop(key)
a.pop("income_in_cr")
print("after pop",a)


#a.get("key")
print(a.get("movie"))           #if not present it give none message

#same as 
print(a["movie"])                #if not present it give error message


#a.copy()
b=a.copy()                      #copy a dict to b


a.clear()                       #clear all dict or remove dict
