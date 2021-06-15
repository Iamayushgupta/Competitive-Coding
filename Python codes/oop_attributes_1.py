class Sample():
    pass


my_sample = Sample()
# print(type(my_sample))
#       OUTPUT = class '__main__.Sample'


class Dog():
    def __init__(self, mybreed):
        # attributes
        self.my_attribute = mybreed


my_dog = Dog(mybreed='huskie')
# print(my_dog.my_attribute)
#       OUTPUT huskie


class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # spots output gonna be true or false
        self.spots = spots


my_dog = Dog(breed='lab', name='oscar', spots=True)
#   print(my_dog.breed) ---- OUTPUT= lab
#   print(my_dog.name)  ------OUTPUT=oscar
#   print(my_dog.spots) -----OUTPUT=True
