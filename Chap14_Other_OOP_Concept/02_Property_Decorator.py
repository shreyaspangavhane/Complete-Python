class Stud():
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

obj=Stud()
obj.name="Shreyas Pangavhane"
print(obj.fname,obj.lname)
