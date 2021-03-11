class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    # METHOD

    def get_cicumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)

print(my_circle.get_cicumference())