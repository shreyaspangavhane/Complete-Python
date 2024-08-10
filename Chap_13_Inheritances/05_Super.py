# super() method is used to access the methods/Constructor of a super class in the derived class.

class Stud():
    name="Shreyas"
    def __init__(self):
        print("This is constructor of Stud class")

class Dept(Stud):
    dept="Computer"
    def __init__(self):
        print("This is constructor of Dept class")

class Collge(Dept):
    college="SCOE"
    def __init__(self):
        super().__init__()
        print("This is constructor of College class")


# a=Stud()              #print only constructor of a class
# print(a.name)


# b=Dept()              #print only constructor of a class
# print(b.dept)


c=Collge()              #Due to super keywpord print all Constructor
print(c.college)
