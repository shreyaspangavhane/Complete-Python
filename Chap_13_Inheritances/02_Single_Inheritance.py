# Single Inheritances
                # ->>Single base class and one child class




class Emp():            # base class
    dept="Developement"
    name="Shreyas"
    def show(self):
        print(f"Name is {self.name} Work in dept {self.dept}")
    

class Coder(Emp):        #derived class
    dept="Testing"
    lang="Python"
    def lang_used(self):
        print(f"The name is {self.name} used languages {self.lang}")

a=Emp()
b=Coder()
print(a.dept,b.dept)

b.lang_used()
b.show()