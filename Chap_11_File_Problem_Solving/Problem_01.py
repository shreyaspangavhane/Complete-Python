# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poems.txt","r") as f:
    contain=f.read()

print(contain)

if("twinkle" in contain):
    print("Word is Present")
else:
    print("Word is Not Present")

