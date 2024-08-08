#  Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
#       ==>> YES

class Sample:
    a="abc"

obj=Sample()
print(obj.a)

obj.a="Def"
print(obj.a)