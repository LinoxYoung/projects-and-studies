def isPowerOfThree(n):
    l = [1]
    i = 1
    while i <= n:
        if n in l: 
            break
        elif l[len(l)-1] > n:
            break
        else:
            l.append(3**i)
            i += 1    
    if n in l:
        return True
    else: 
        return False

