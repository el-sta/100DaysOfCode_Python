#Day 5 Project: Password Generator 

#import libraries
import random

#create the lists of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#Hard Version:password does not follow a pattern
#Ask user for number of characters
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty list to hold the password characters
password = []

#Add an item to the end of the list using append
for l in range(nr_letters):
    password.append(random.choice(letters))
for s in range(nr_symbols):
    password.append(random.choice(symbols))
for n in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the list
random.shuffle(password)

#Print the password list as a string using .join()
print("Your password is:")
print("".join(password))
print(f"Your password is:".join(password))