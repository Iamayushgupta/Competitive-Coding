class Dog():
  species='mammal'
  def __init__(self,breed,name,spots):
    self.breed=breed
    self.name=name
    self.spots=spots
  def bark(self,number):
    print("woof! my name is {}, number is {}".format(my_dog.name,number))
  
my_dog=Dog('lab','oscar','True')
#  print(my_dog.species)---- OUTPUT ---mammal

my_dog.bark(2)
#  OUTPUT ------ woof! my name is oscar, number is 2


class Circle():
  #class object attribute
  pi=3.14
  def __init__(self,radius=1):
    self.radius=radius
    
  def get_circumference(self):
    return self.radius*self.pi*2
    # or Circle.pi

my_circle=Circle()
#print(my_circle.get_circumference())
#OUTPUT= 6.28

