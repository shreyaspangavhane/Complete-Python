a=(1,26,"Tony","Stark",26,3,True)


#count(ele) -> print occurance of ele
print(a.count(26))     


#how to do changes in tuple   ->steps:
        # 1) Convert tuple into list
        # 2) Perform Operation
        # 3) Convert list into tuple
a=(1,26,"Tony","Stark",26,3,True)
b=list(a)
b.append("Shreyas")
a=tuple(b)
print(a)


#join tuple
t1 = ("a", "b" , "c")
t2 = (1, 2, 3)
t3 = t1 + t2
print(t3)

#packing amd unpacking 
# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


