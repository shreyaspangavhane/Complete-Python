with open("python.txt","r") as f:
    content=f.read()

lowerContent=content.lower()
if ("python" in  lowerContent):
    print("Yes, Present")

else:
    print("Not Present")
    