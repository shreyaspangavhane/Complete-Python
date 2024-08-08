# here the greet function is the static b/c it not use any variable of class
#for that instead of giving them  SELF parameter use @staticmethod before function


class Stud():
    name="Shreyas"
    dept="Computer"

    #static method
   
    @staticmethod
    def greet():
        print("Hello,Connection")


s=Stud()
s.greet()