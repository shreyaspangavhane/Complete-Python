# It is used to stop current iteration of loop and continue to next

for i in range(1,10):
    print("display")
    if(i==7):
        continue
    print(i)
    i+=1