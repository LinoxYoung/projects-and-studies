def x(y):
    try:
       return float(y)
    except:
       return None
Amount = (input("amount: "))
Rate = (input("interest rate: "))
Time = (input("time: "))
Intest = (input("interest: "))
A = x(Amount)
R = x(Rate)
T = x(Time)
I = x(Intest)
def simple(A, R, T, I):
   if T != None and R != None and A != None and I == None:
      return f"simpes interest is {T * R * A} \nfature value is {(T * R * A) + A}"
   elif T == None and R != None and A != None and I != None:
      return f"time is {I/(A*R)}"
   elif T != None and R == None and A != None and I != None:
      return f"rate is {I/(A*T)}"
   elif T != None and R != None and A == None and I != None:
      return f"rate is {I/(R*T)}"
simple = simple(A, R, T, I)
print(simple)

