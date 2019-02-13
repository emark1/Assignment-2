#Factorial

user_number = int(input("Please enter a number: "))

for index in range(1,user_number):
    user_number = user_number * index    

print(f"The factorial is {user_number}")