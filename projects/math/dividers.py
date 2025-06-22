number = int(input("number: "))
def dividers(number):
    y = []
    x = 0
    for x in range(number):
        x += 1
        if number%x == 0:
            y.append(x)
    return(len(y))
print(dividers(number))