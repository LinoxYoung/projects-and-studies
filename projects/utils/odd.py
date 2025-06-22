y = int(input("number: "))
def value(y):
    if y%2 == 0:
        return f"{y} is even"
    else:
        return f"{y} is old"
value = value(y)
print(value)

X = float(input("what number?"))
def odd_or_even(X):
    if ".0" in str(X/2):
        return "even"
    else:
        return "odd"
odd_or_even = odd_or_even(X)
print(odd_or_even)