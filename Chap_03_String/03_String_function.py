name="Shreyas"


#len()
print(len(name))


#endswith
print(name.endswith("as"))          #check string end with as or not if yes then print True


#starts with 
print(name.startswith("as"))        #check string starts with as or not if yes then print True 


# capitalize                    #make 1st letter as capitals
print(name.capitalize())


#string.count("c") – counts the total number of occurrences of any character.
count=name.count("S")
print(count)


#uppercase
name="Shreyas"
print(name.upper())


#lowercase
name="Shreyas"
print(name.lower())


#Remove Whitespace-> strip
name="Shreyas Pangavhane"
print(name.strip())


#find word      ->print the index of that word
print(name.find("yas"))


#string.replace (old word, new word )
print(name.replace("Sh","sh"))

