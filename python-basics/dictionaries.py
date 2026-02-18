#Name : Patience Mukuhi Gichango 
#Date : 18/2/2026
# Program to show dictionaries in python
# Dictionary of cars

cars = {"Model" : "Falcon Defender",
         "Make" : "Defender",
         "Colour" : "Peach",
          "Year" : "2026" }

print(cars["Model"])
print(cars["Year"])

students = {"Alice":24,
                  "James":18, 
                  "Wayne":21,
                  "Daisy":37}

for key in students:
    print(key) 

for val in students.values():
    print(val) 
 