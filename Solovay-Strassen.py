from Jacobi import Jacobi
from Power import Power
import random

def Solovay(n:int):
    a = random.randint(1,n-1)
    x = Jacobi(a,n)
    if x == 0:
        return "n is composite"
    else:
        s = (n-1)/2
        s = int(s)
        y = Power(a,s,n)
        if x%n == y%n :
            return "n is prime"
        else:
            return "n is composite"
