dic = {
    "apple" : 600,
    "banana" : 2000,
    "orange" : 400,
    "strawberry" : 200,
    "grape" : 4000,
    "lemon" : 700,
    "watermelon" : 600, 
    }
minV = int(input("value minimum: "))
maxV = int(input("value maximum: "))
def filter(dic, maxV, minV):
    new_list = []
    list_dic_V = (list(dic.values()))
    list_dic_K = (list(dic.keys()))
    for cmprs in range(len(dic)):
        if minV < (list_dic_V[cmprs]) < maxV:
            (new_list.append((list_dic_K[cmprs])))
    return new_list        
print(filter(dic, maxV, minV))