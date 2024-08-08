# Create a class “Programmer” for storing information of few programmers working at Microsoft
class Programmer():
    company="Microsoft"
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary

obj=Programmer("Shreyas","Computer",980000)
print(f"name is {obj.name}\ndept is {obj.dept}\nSalary is {obj.salary}")
