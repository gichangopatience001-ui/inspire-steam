#Name : Patience Mukuhi Gichango 
#Date : 19/02/2026
# Program to show inheritance in python

class Animal():
    def __init__ (self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.5 * weight
        print(f"The animal weighs {weight} kgs")

    def eat(self,food):
        print(f"The animal eats {food}")

class Dog(Animal):
    
    def __init__ (self,colour,height,breed):
        super().__init__(species,weight,food)
        self.colour = colour
        self.height = height
        self.breed = breed
    
    def barks(self):
        print(f"The dog says woof wooof")

    def eat(self,food):
        print(f"The animal eats {food}")
 
class Horse(Animal):
    def __init__ (self,colour,weight,breed):
        self.colour = colour
        self.weight = weight
        self.breed = breed
    
    def neigh(self):
        print(f"The horse says neigh neigh")


        