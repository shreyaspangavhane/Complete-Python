f=open("read_file.py","r")
print(f.read())
f.close()

#same can be done using with statement. here there is no need to close file

with open("read_file.py") as f:
    print(f.read())

#do not need to close file