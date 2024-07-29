name="Iron Man"

#calculate lenth using len()
length=len(name)
print("length is:",length)


# slicing
shortname=name[0:6]     # same as name[:6]      starts from 0 and end on 5th
print(shortname)


#slicing
print(name[1:])         #same as name[1:7]


#Negative Slicing
print(name[-4:-1])


#print speacific char
charc1=name[1]
print(charc1)


#skip value as a part of our slice
fname="Tony Stark"
print(fname[1:6:2])