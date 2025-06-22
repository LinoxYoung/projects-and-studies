while True:
    Menu = int(input("1 for quadratic equation, 2 for pythagoras, 3 area:"))
    if Menu > 3:
        print("erro")
    if Menu == 1:
        A = float(input("A:"))
        B = float(input("B:"))
        C = float(input("C:"))
        def quadraticaquation(A,B,C):
            Delta = ((B**2-(A*4*C)))
            if A == 0:
                return"this is not a quadratic equation"
            elif Delta > 0:
                return f" A: {A} B: {B} C: {C} \n Delta {Delta} \n quadratic equation solution \n X1 = {((-B+(Delta**0.5))/(2*A))} \n X2 = {((-B-(Delta**0.5))/(2*A))}"
            elif Delta == 0:
                return f"A: {A} B: {B} C: {C} \n Delta {Delta} \n quadratic equation solution \n X1 {((-B+(Delta**0.5))/(2*A))}"
            elif Delta < 0: 
                return f"Not Delta"           
        quadraticaquation = quadraticaquation(A,B,C)
        print(quadraticaquation)
    if Menu == 2:
        def number(value):
            try:
                return int(value)
            except:
                return None
        C1 = (input("cateto1:"))
        C2 = (input("cateto2:"))
        H = (input("hypotenuese:"))
        C1 = number(C1)
        C2 = number(C2)
        H = number(H)
        def pythagoras(C1, C2, H):
            if C1 == C2 == H:
                x = 0
                while x <= H-1:
                    x += 1
                    print("*" * x)
                return f"Area is {(H**2)/2}"
            elif H is None and C2 is not None and C1 is not None:
                return f"hypotenuese = {(C1**2 + C2**2)**0.5}"
            elif H is not None and C2 is None and C1 is not None:
                return f"cateto2 = {(-C1**2+H**2)**0.5}"
            elif H is not None and C2 is not None and C1 is None:
                return f"cateto1 = {(-C2**2+H**2)**0.5}"
            elif C1**2 + C2**2 == H**2:
                return f" {C1**2} + {C2**2} == {H**2}"
            else:
                return "erro"
        pythagoras = pythagoras(C1, C2, H)
        print(pythagoras)
    if Menu == 3:
        shape = input("name: ")
        y = input("side or ray: ")
        z = input("height: ")
        def calculate_area(shape, y, z=None):
            if shape == "t" or shape == "triangle":
                return (y*z)/2
            elif shape == "r" or shape == "rectangle":
                return y * z
            elif shape == "q" or shape == "square":
                return y ** 2
            elif shape == "c" or shape == "circle":
                return 3.14*y**2
        print(calculate_area(shape, y, z=None))