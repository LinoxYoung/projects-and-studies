y = float(input("number:"))
def factorial_(y):
    x = int(y)
    y = 1 
    z = 1
    while z <= x:
        y *= z
        z += 1 
    return(y)
factorial_ = factorial_(y)
print(factorial_)
