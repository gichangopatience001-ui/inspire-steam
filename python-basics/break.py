#Name : Patience Mukuhi Gichango 
#Date : 17/02/2026
# Program to illustrate how to break in python

number = 1 
while number <10:
    print(number)
    # number = number + 1
    number += 1
    # number *= 2
    if number == 4:
        break
    # number +=1
    print("Breaking from the loop")
    continue

