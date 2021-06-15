class Animal():
    def __init__(self):
        print("animal created")
    def who_i_am(self):
        print("i am an animal")
    def eat(self):
        print("i am eating")


my_animal=Animal()
my_animal
# OUTPUT= animal created

my_animal.eat()
# OUTPUT = i am eating


## INHERITANCE
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created")
    def who_i_am(self):
        print("i am a dog")
        # overwritten on class animal

mydog=Dog()
mydog.who_i_am()
# OUTPUT= animal created,dog created, i am a dog

class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says meow!"

oscar=Dog("oscar")
kiki=Cat("kiki")

print(oscar.speak())
#OUTPUT= oscar says woof!


##POLYMORPHISM

for pet in [oscar,kiki]:
    print(type(pet))
    print(type(pet.speak))

def pet_speak(pet):
    print(pet.speak())

pet_speak(kiki)
#OUTPUT= kiki says meow!

class Phylum():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("subclass")

class Dog(Phylum):
    def speak(self):
        return self.name + " says woof"

bambo=Dog("bambo")
print(bambo.speak())