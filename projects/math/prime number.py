number = int(input("number: "))
def prime(number):
    i = 2
    while i <= number-2:
        i += 1
        if number%i == 0 :
            return f"{number} is not a prime"
        i += 1
    return f"{number} is a prime"
prime = prime(number)
print(prime)