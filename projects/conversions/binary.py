
def binary(number):
    y = []
    x = 1
    while x <= number:
        y.append(number%2)
        number = number//2
  
    z = (y[::-1])
    list_z = [str(n) for n in z]
    return(int("".join(list_z)))
print(binary(5))