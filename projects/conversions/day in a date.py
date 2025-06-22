#31/03/2010 08/06/2025 09/04/2005
date = input("date: ").split()
dateX = date[0].split('/')
dateY = date[1].split('/')
X = dateX
Y = dateY
def day(X, Y):
    if int(X[0]) <= 31 and int(Y[0]) <= 31:
        if int(X[1]) <= 12 and int(Y[1]) <= 12:
            if int(X[0]) != int(Y[0]) and int(X[1]) == int(Y[1]) and int(X[2]) == int(Y[2]):
                return f"days: {int(Y[0]) - int(X[0])}"
            elif int(X[0]) != int(Y[0]) and int(X[1]) != int(Y[1]) and int(X[2]) == int(Y[2]):
                return f"days: {int(Y[0]) - int(X[0])+31*(int(Y[1]) - int(X[1]))}"
            elif int(X[0]) != int(Y[0]) and int(X[1]) != int(Y[1]) and int(X[2]) != int(Y[2]):
                 return f"days: {int(Y[0]) - int(X[0])+31*(int(Y[1]) - int(X[1])) +365*(int(Y[2]) - int(X[2]))}"
            elif X == Y:
                return f"{0}"
print(day(X, Y))