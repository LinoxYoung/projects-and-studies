number = (input("list: ")).split()
def arithmeticmean_mean_median(number):
    y = (list(map(int, number)))
    x = sorted(y)
    print (f"mean {(sum(y)/len(y))}")
    if len(x)%2 == 0:
        return f"median {((((x[(int(len(x)/2))]) + (x[(int(len(x)/2-1))]))/2))}"
    else:
        return f"median {(x[(((len(x))/2))])}"
arithmeticmean = arithmeticmean_mean_median(number)
print(arithmeticmean)
