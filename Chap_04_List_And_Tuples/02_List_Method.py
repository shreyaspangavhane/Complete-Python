friends=["Tony","Stark",23.4,"Jarvis","Stark",60]

print(friends)


#Append method
friends.append("Iron_Man")
print(friends)


#sort() method
l1=[1,45,23446,567,2,679,23]
l1.sort()
print(l1)


#sort reverse order
l1=[1,45,23446,567,2,679,23]
l1.sort(reverse=True)
print(l1)


#reverse method                 ->starts from end to 1st point
l1=[1,45,23446,567,2,679,23]
l1.reverse()
print(l1)


#insert(idx,ele)
friends.insert(5,"Marvel")       #add Marvel at 5th idx
print(friends)


#pop(idx)       ->delete the ele at that pos
friends.pop(4)
print(friends)


#remove(ele)
friends.remove(60)
print(friends)


#in method     ->Check the ele is present in list or not
if "Tony" in friends:
    print("Present")


# Join Two Lists
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
l3 = l1 + l2
print(l3)