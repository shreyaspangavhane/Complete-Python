# Read the data From File

# f= open("file.txt")             #default open file in read

#for open file in read mode
f= open("D:/COURSES/Python for Data Science/Chap_10_File/read_file.txt","r")

data= f.read()
print(data)
f.close()

