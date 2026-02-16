#Name : Patience Mukuhi Gichango 
#Date : 13/02/2026
# Program to calculae arithmetic progression

# Calculate the nth term

a = int(input("Enter the first number:"))
n = int(input("Enter the number of terms:"))
d = int(input("Enter the common differnce:"))

nth_term = a+(n-1) * d
sn = (n/2) * ((2 * a) + ( n - 1 ) * d)
print(f"The nth term is :{nth_term}")
print(f"The sum of the numbers is:{sn}")

