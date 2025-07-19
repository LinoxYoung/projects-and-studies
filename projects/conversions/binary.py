def convert(number):
    y = []
    x = 1
    while x <= number:
        y.append(number%2)
        number = number//2
  
    z = (y[::-1])
    list_z = [str(n) for n in z]
    return(int("".join(list_z)))
print(convert(5))

def deconvert(number):
    l = []
    number = str(number)
    number = list(number)[::-1]
    for i in range(len(number)):
        l.append(int(number[i])*2**i)
    return(sum(l))
print(deconvert(101))
