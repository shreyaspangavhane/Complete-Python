f=open("D:/COURSES/Python for Data Science/Chap_10_File/read_file.txt")

line=f.readlines()
print(line)


# print one one line

line1=f.readline()
print(line1)

line2=f.readlines()
print(line2)

line3=f.readlines()
print(line3)

line4=f.readlines()
print(line4)


# print all line at a time using while loop
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
    

f.close()           #close the file