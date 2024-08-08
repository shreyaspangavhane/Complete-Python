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



a=Calculator(4)

a.square()
a.cube()
a.sqroot()