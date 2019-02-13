#Prime Number Check
def primecheck():
    number = int(input("Please enter a number: "))
    text = ""
    if number == 2 or number == 1:
        text = "Prime number."

    for index in range(number-1,1,-1):
        if number % index == 0:
            text = "This is not a prime number."
            break
        else: 
            text = "This is a prime number."

    return text

print(primecheck())