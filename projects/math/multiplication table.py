x = int(input("number: "))
def multiplicationtable(x):
    z= []
    y = 0
    while y <= 9:
        y += 1
        z.append(y*x)
    return z
print(multiplicationtable(x))