#Name : Patience Mukuhi Gichango 
#Date : 19/02/2026
# Program to run the same instructions

def cook_egg():
    oil = "20ml"
    pan = True 
    moto = True
    eggs = 2
    print(f"The pan is {pan}, and the fire is {moto}, and {oil} amount of oil andcook {eggs} eggs")

print("Here is statement 1")  

print("Here is statement 2")  

cook_egg()

print("Here is statement 3")  

# Bus fare creating function

def create_fare(route, distance, is_rush_hour):
    fare = distance * 10
    if is_rush_hour == True:
        fare = fare*1.5
    print(f"Your fare on route {route} is {fare}")

    return fare

rush_hour = True

returned_fare = create_fare("Juja-Allsops", 7, rush_hour)
print(f"The fare returned is: {returned_fare}")

# Passing a list as a parametre
def write_all_interests(interests):
    for interest in interests:
        print(f"Iam interested in {interest}")

all_interests = ("Painting","Baking","Cooking","Singing","Watching kdrama")
write_all_interests(all_interests)