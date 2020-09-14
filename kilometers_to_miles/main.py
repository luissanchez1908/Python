# Create a program that asks the user for a number of kilometers,
# converts it to Miles and prints the result
#1 mile = 1.609344 km

user_input = float(input("Please enter the kilometers do you want to convert in miles: "))
miles = user_input / 1.609344

print("Kilometers in miles are: ", round(miles, 2))

