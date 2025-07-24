def happy_number(n):
    def count(x):
        l = []
        x = list(str(x))
        for i in range(len(x)):
            l.append((int(x[i]))**2)
        return sum(l)
    while True:
        print(n)
        n = count(n) 
        if count(n) < 9:
            break
    if count(n) == 1:
        return True
    else:
        return False
