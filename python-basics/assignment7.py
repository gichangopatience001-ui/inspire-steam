#Name : Patience Mukuhi Gichango 
#Date : 17/02/2026
# Program to display diamond 

rows = 5 # You can change this number

print("------DIAMOND------")
# Upper part
for i in range(rows):
    print(" " * (rows -i - 1) + "*" * (2 * i + 1))

# Lower part
for i in range(rows - 2, -1, -1):
    print(" " * (rows -i -1) + "*" * (2 * i + 1))

print("------CENTERED TRIANGLE------")
# Program to display a triangle
for i in range(rows):
    print(" " * (rows -i - 1) + "*" * (2 * i + 1))

print("------RIGHT ANGLED TRIANGLE------")
# Method two
rows = 5 
for i in range(1, rows + 1):
    print("*" * i)

# Program to solve quadratic equation
import math

# Take input from user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real and different roots:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif discriminant == 0:
    root = -b / (2*a)
    print("One real root:")
    print("Root =", root)

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("Two complex roots:")
    print("Root 1 =", real_part, "+", imaginary_part, "i")
    print("Root 2 =", real_part, "-", imaginary_part, "i")