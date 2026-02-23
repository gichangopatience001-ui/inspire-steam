#Name : Patience Mukuhi Gichango 
#Date : 19/02/2026
# Program to show classes in python

class Car():
    # Atttributes of the car
    def __init__ (self,model,make,colour,year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year
    
    # print cars
    def print_details(self,model,make,colour,year):
        print("{make}, {model}, of colour {colour}, made in {year}")

# instantiate a class object

my_car = Car("Atenza","Mazda", "black","2022")
dad_car = Car("Land cruiser","Toyota","white","2022")

my_car.print_details("Atenza","Mazda","black","2022")
dad_car.print_details("Land cruiser","Toyota","white","2022")


     



