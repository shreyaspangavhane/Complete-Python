# methods()

s={2,6,3,54,7,1}

#cal length
print(len(s))


#add(ele)
s.add(4)
print(s)

a={3,98,34,12}
s.update(a)                 #here use update to add one set to the another
print("set s",s)


#remove(ele)
s.remove(54)
print(s)


#pop(ele)       remove the random element
s.pop(54)
print(s)



#s.clear()          do empty all set
s.clear()
print(s)