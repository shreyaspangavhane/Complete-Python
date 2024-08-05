# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt","r") as f:
    content1=f.read()

with open("copy_this.txt","r") as g:
    content2=g.read()

if(content1==content2):
    print("File content is Same")

else:
    print("File content is Not Same")
    