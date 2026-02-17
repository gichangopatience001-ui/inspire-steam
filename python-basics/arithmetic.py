#Name : Patience Mukuhi Gichango 
#Date : 17/02/2026
# Program to perform arithmetic opperations

f_number = 12
s_number = 34
sum_numbers = f_number + s_number
product_numbers = f_number * s_number
difference_numbers = f_number - s_number
quocient_numbers = f_number / s_number

print("The sum of the numbers %d "%sum_numbers)
print("The quocient of the numbers %0.2f "% quocient_numbers)
print("The product of the numbers %d "%product_numbers)
print("The difference of the numbers %d"%difference_numbers)

#modulus - remainder
print(7%5) 

# even and odd sum_numbers
# for x in range (0,21):
    # if (x%2)==1:
    #     print("Even number")
    # else:
    #     print("Odd number")
    # print(x)

for x in range (0,21):
    if(x%2==1):
        print(f"{x} is odd number")
    elif(x%2==0):
        print(f"{x} is an even number")
 
    