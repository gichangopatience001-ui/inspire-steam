#Name : Patience Mukuhi Gichango 
#Date : 18/2/2026
# Program to show lists in python
# List of friends
friends = ["Rachel","Phoebe","Ross","Monica", "Chandler","Joy"]
print(friends)

friends.sort()
print(friends)\

friends.reverse()
print(friends)

friends.append("Jack")
print(friends)

new_friends = ["Patience","Keshi","Wayne","Zayn"]

print(len(new_friends))

# new list of students
students = friends + new_friends
print(students)

students.pop()
print(students)

students.insert(5,"Kamanja")
print(students)

students.insert(9,"Celestine")
print(students)

students.extend("Samantha")
print(students)

students.remove("Celestine")
print(students)

new_students = students.copy()
print(new_students)

