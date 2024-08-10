# MultiLevel Inheritances
    # there are one parent class and one child class and this child class is parent for another child class

class Emp():            # base class
    dept="Testing"
    name="Shreyas"
    def show(self):
        print(f"Name is {self.name} Work in dept {self.dept}")
    

class Coder(Emp):        #derived class
    lang="Python"
    def lang_used(self):
        print(f"Dept {self.dept} used languages {self.lang} for their Work")


class Company(Coder):   #Derived class

    def emp_data(self):
        print(f"Emp name is {self.name}\nDept is {self.dept}\nLang used {self.lang} ")


a=Emp()
b=Coder()
c=Company()

a.show()        #for the Emp class
print("")

b.show()        #for the Coder Class
b.lang_used()   
print("")

print("")       #for the Company Class
c.show()
c.lang_used()
c.emp_data()