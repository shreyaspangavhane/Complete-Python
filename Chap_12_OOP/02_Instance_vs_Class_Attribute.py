# instance Attribute having high priority than class attribute
        #flow:
                # 1.check attribute Present in object/instance
                # 2.then go for Class  Attributes

class Stud():
    name="Shreyas"
    dept="Computer"

s=Stud()

s.name="Ajit"       #creating instance attribute

print(s.name,s.dept)           