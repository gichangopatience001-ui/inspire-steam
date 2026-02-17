#Name : Patience Mukuhi Gichango 
#Date : 13/02/2026
# Program to calculate geometric progression

a = int(input("Enter the first number":))
r = int(input("Enter the common ratio:"))
n = int(input("Enter the number of terms:"))

nth_term = (a*r)**(n-1) # a*r raised to the power of (n-1)
sn = (a*(1-r**n))/(1-r)

print(f"The nth_term is : {nth_term}")
print(f"The sum of the numbers is : {sn}")
