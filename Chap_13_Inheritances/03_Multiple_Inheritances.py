# Multiple Inheritances
    # there are two parent class and one child class

class Emp():            # base class
    dept="Testing"
    name="Shreyas"
    def show(self):
        print(f"Name is {self.name} Work in dept {self.dept}")
    

class Coder():        #derived class
    lang="Python"
    def lang_used(self):
        print(f"\nDept {self.dept} used languages {self.lang} for their Work")


class Company(Emp,Coder):   #Derived class

    def emp_data(self):
        print(f"\nEmp name is {self.name}\nDept is {self.dept}\nLang used {self.lang} ")


a=Emp()
b=Coder()
c=Company()

c.show()
c.lang_used()
c.emp_data()