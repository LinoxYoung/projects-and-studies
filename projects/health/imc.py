weight = int(input("your weight: "))
height = float(input("your height: "))
imc = weight/(height**2)
def count(imc):
    if imc < 17:
        return f"Very underweight {imc}"
    elif imc < 18.5:
        return f"Underweight {imc}"
    elif imc < 25:
        return f"Normal weight {imc}"
    elif imc < 30:
        return f"Overweight {imc}"
    elif imc < 35:
        return f"Grade 1 obesity {imc}"
    elif imc < 40:
        return f"Grade 2 obesity {imc}"
    else:
        return f"Grade 3 obesity {imc}"
count = count(imc)
print(count)