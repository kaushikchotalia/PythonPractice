# basic class creation
class Sample():
    pass

# creating instance of the class
my_sample = Sample()

print(type(my_sample))

print('-------------------------------------------------------')

# create class do and a method
# __init__ constructor for a call
class Dog():
    # CLASS OBJECT ATTRIBUTES
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self,mybreed,name,spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.myattribute = mybreed
        # as per standard it should be written as
        # self.breed = breed
        self.name = name

        # Ex[ect boolean True/False
        self.spots = spots

# OPERATIONS/Actions ---- > Methods
    def bark(self):
        print("WOOF! My name is {}".format(self.name))

my_dog = Dog(mybreed='Lab',name='Sammy',spots=False)

print(type(Dog))
print(my_dog.myattribute)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark())
print('-------------------------------------------------------')

