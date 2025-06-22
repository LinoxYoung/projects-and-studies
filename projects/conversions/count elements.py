x = [1,4,5,6,3,6,1,6,1,61,5]
y = 6
def count_elements(x,y):
    z = []
    x = x.copy()
    if y in x:
        while y in x:
            x.remove(y)
            z.append(y)
        return f"{y} was found {len(z)} times in the list"
    else:
        return f"{y} is not on the list"
print(count_elements(x,y))

print(x)