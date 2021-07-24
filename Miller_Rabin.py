from Jacobi import Jacobi
from Power import Power
import random

def Miler(n:int):
    t = 0
    r = n-1
    while r%2 == 0:
        r = r//2
        t+=1
    a = random.randint(1, n - 1)
    b = Power(a,r,n)
    if b%n == 1:
        return "n is prime"
    i = 0
    while i<t:
        if b%n == n-1:
            return "n is prime"
        else:
            b = Power(b,2,n)
        i+=1
    return "n is composite"
