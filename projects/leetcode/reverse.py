number = int(input("number: "))
def reverse(x):
    if x < 0:
        x = list((str((x)*-1)[::-1]))
        while list((str(x)[::-1]))[0] == "0":
            x.remove("0")
        if ((int("".join(x)))) >= 2**32 -1:
            return 0
        else:
            return ((int("".join(x))))
    elif x >= 0:
        x = list((str((x))[::-1]))
        while list((str(x)[::-1]))[0] == "0":
            x.remove("0")
        if ((int("".join(x)))) >= 2**32-1:
            return 0
        else:
            return ((int("".join(x))))
print(reverse(number))
