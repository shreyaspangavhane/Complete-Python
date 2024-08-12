# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Two_D_vector():
    vector="2D"

class Three_D_vector(Two_D_vector):
    vactor2="3D"

obj=Three_D_vector()
print(obj.vector,obj.vactor2)