year = int(input("year: "))
def leapyear(year):
    if year%4 == 0:
        return f"{year} is a leapyear"
    else:
        return f"{year} is a not leapyear"
leapyear = leapyear(year)
print(leapyear)