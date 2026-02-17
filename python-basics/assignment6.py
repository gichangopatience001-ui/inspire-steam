#Name : Patience Mukuhi Gichango 
#Date : 16/02/2026
# Program to calculate income tax

salary =int(input("Enter your gross salary"))

# if salary < 50000:
#     tax = (2.5 * salary)/100
#     net_salary = salary - tax

# if 50000 < salary < 100000 :
#     tax = (4.5 * salary)/100
#     net_salary = salary - tax 

# if salary > 100000 :
#     tax = (7.5 * salary)/100
#     net_salary = salary - tax

# print(f"Gross salary = {salary}")
# print(f"Net salary = {net_salary}")
# print(f"Tax = {tax}")

if salary < 50000:
    tax_rate = 2.5
elif salary <= 100000:
    tax_rate = 4.5
else :
    tax_rate = 7.5
tax = (tax_rate * salary)/100
net_salary = salary - tax 

print(f"Gross salary = {salary}")
print(f"Tax rate applied = {tax_rate}%")
print(f"Net salary = {net_salary}")
print(f"Tax = {tax}")


    
