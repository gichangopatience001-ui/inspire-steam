#Name : Patience Mukuhi Gichango 
#Date : 24/02/2026
# Program to perform file operations in python 
# Create to the new File 
new_file = open("Student_data.txt","r+")


# Write to new file 
new_file.write("{ Student name : Dove Cameroon, ID : 1234321,Email : dovecamerroon@gmailcom } ")
new_file.close()


# Read from the new file
new_file = open("Student_data.txt","r+")
data = new_file.read()
print(data)
new_file.close()


# Delete a file
# use os module 
import os 
os.remove("remove.txt")

# Delete a folder
os.rmdir("folder")

