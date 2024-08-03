# for loop is used to iterate through a sequence like list, tuple, or string [iterables]

l1=[1,2,5,3,8]
for item in l1:
    print(item)


#range function
for i in range(4):
    print("\n",i)        #print 0 to 3


#range function with start,stop and step size
for i in range(2,10,2):
    print(i)


# FOR LOOP WITH ELSE
print("\n")
for i in range(2,10,2):
    print(i)
else:
    print("Done")