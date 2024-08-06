#class name first letter shuld be start with capital

class Stud():
    name="Shreyas"              # class attributes
    dept="Computer"
    rn=110

s=Stud()            #creating Object s
print(s.name,s.dept)

#creating more object
a=Stud()
print(a.rn,a.dept)


s.yr="T.Y"          #instance/object attributes
print(s.name,s.yr,s.dept)       #here yr is object/instance attribute and name,rn and dept is class attribute

