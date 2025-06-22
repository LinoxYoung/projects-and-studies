X = int(input("What temperature do you want? 1 for fahrenheit and 2 for kalvin: "))
C = float(input("temp:"))
def temperature(C,X):
    if X == 1:
        return f"Fahrenheit: {(C * 9/5) + 32}"
    if X == 2:
        return f"Kelvin: {(C + 273.15)}"
temperature=temperature(C,X)
print(temperature)