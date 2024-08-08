# Add a static method in problem 2, to greet the user with hello.


# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"Square is: {self.n*self.n}")

    def cube(self):
        print(f"Cube is: {self.n*self.n*self.n}")

    def sqroot(self):
        print(f"Square Root is: {self.n**1/2}")

    @staticmethod
    def Greet():
        print("Thank You!!")

a=Calculator(4)

a.square()
a.cube()
a.sqroot()
a.Greet()
