class A():
    a=2
    @classmethod
    def printing(cls):
        print(f"The value of class Attribute is {cls.a}")

obj=A()
obj.a=34            #instance Attribute

obj.printing()      #print the value of class attributre a=2 intead of a=34