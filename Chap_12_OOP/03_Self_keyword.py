# self keyword it is used to give access right to function inside the class
                #neither U use the variable of that or not it is mandatory

class Stud():
    name="Shreyas"
    dept="Computer"

    #function with use of class variable
    def getRecord(self):        
        print(f"Name is:{self.name}\nDept is {self.dept}")

    #function with Not use of class variable
    def greet(self):
        print("Hello,Connection")

s=Stud()

s.getRecord()

# same as :
# Stud.getRecord(s)

s.greet()