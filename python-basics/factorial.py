#Name : Patience Mukuhi Gichango 
#Date : 16/02/2026
# Program to calculate the factorial off numbers
factorial = 1 #initialize factorial 1
number =int (input("Enter the number n :"))
for n in range (1,number+1):
    factorial*=n

print(f"{number}!={factorial}")


