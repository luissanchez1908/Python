#create a program that asks the user for his first name, his middle name and his last name. the print:
#"your initials are ___"

name = input("Please enter your name: ")
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")


print("Your initials are: ", name[:1], " ", middle_name[:1], " ", last_name[:1])
