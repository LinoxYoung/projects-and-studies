yourname = input("What your name:")
value = int(input("What price of products:"))
product = int(input("What products: "))
def discount(yourname, value, product):
    print f" Welcome {yourname} \n This is the value {value} \n This is the products: {product} \n price without discount: {value * product}"
    if value * product < 2.500:
        print ("price with discount:", value * product)
    elif value * product >= 2500 and value * product < 6000:
        print ("price with discount:", -(value * product * 0.04) + value * product)
    elif value * product >= 6000 and value * product < 10000:
        print ("price with discount:", -(value * product * 0.07) + value * product)
    elif value * product > 10000 :
        print ("price with discount:", -(value * product * 0.11) + value * product) 
discount=discount(yourname, value, product)
print(discount)