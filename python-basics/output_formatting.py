#Name : Patience Mukuhi Gichango 
#Date : 17/02/2026
# Program to format the output in different types

name = "Patience Mukuhi" 

weight = 85 # weight in kgs

fav_kdrama = "Buried hearts"

height = 150.90 #height in cms

# 1. Format using printf(f"{}")

print(f"My name is {name} and I weigh {weight}kgs. ")

# 2. Using f string
msg = f"My name is {name} and my favourite kdrama is {fav_kdrama}."
print(msg)

# 3. Using {} and .format() 

print("My name is {0} and i am {1} cms tall".format(name,height))

# 4. Using output specifiers %s_strings %d_integers %f_float

import maths
print("The value of pi is approximately")
print("My favourite kdrama is s%" %fav_kdrama)
