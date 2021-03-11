class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

class Dog(Animal):

    species = 'mammal'
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am a Dog")
    def eat(self):
        print("I a dog and eating")


myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()

print("---------------------------------------------------------")

mydog = Dog()
mydog.who_am_i()
mydog.eat()
