#Name : Patience Mukuhi Gichango 
#Date : 19/02/2026
# Program to create classes

class Human : 
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True 
    warm_blooded = True
    city = "New York"

    # We then create the constructor of the class object
    # The constructor will be used to create copies of this object
    def __init__(self, name, age):
        self.human_name = name 
        self.human_age = age

    def tell_story(self):
        print(f"Hello I am {self.human_name}. Here is a story")
        print("I was a girl in a village doing alright then i became a princess overnight. ")

# Create the humans
wayne = Human("Sofia", 17)
patience = Human("Patience", 21)

# Let the humans created do the things
patience.tell_story()
print("Patience's age is: patience_human_age ")

wayne.tell_story()
print("Wayne's age is: wayne_Human_age ")

# Modify one of the objects, without modifying other objects
print("Sofia's location:", patience.city)
print("Cameroon's location:", wayne.city)
 
patience.city = "Kenya"

