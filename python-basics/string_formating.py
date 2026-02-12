#Name : Patience Mukuhi Gichango
#Date : 12/02/026
#String_formating

#Get strinng length
sentence = "I watch K-Drama"

string_length = len(sentence)

print(f"The length is: {string_length}")
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is:",split[0])

# Make everything CAPS
mpesa_code = "asdert34qw"

capitalized = mpesa_code.upper()

print("New mpesa_code:", capitalized)

#Make to lower
mpesa_code = "ASDERT34QW" 

small_letters = mpesa_code.lower()

print("New mpesa_code:",small_letters)

#Replacing characters in a string

balance = "1000kes"
amount_added = "12.90kes"

cleaned_balance = balance.replace("kes", "")

print("Cleaned balance:", cleaned_balance)

cleaned_amount_added = amount_added.replace("kes","")

print("cleaned_amount_added:",cleaned_amount_added)

new_balance = int(cleaned_balance) + float(cleaned_amount_added)

print("new_balance is:", new_balance)


#M_pesa balance
sentence_3 = "confirmed you have recieved 40kes from Phllip"
split = sentence_3.split(" ")
print(f"The first subject is:",split[4])

balance_2 = "23.09kes"
amount_added_2 = "40kes"

cleaned_amount_added_2 = amount_added_2.replace("kes:"," ")
print("cleaned_amount_added:", cleaned_amount_added_2)
