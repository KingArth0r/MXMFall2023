import numpy as np
import sympy as sp

x = sp.symbols('x')

def generate_sequences(f, p,n, valuerange,length):

    polynomial = sp.Poly(f, x)
    for i in range(n,n+valuerange):
        modsequence=np.zeros(length)
        startingvalue = i
        modsequence[0]=startingvalue % 3
        for j in range(1, length):
            check = (polynomial.subs(x,modsequence[j-1]) / p)
            if check.is_integer:
                modsequence[j] = ((polynomial.subs(x, modsequence[j - 1]) / p) % p)
            else:
                modsequence[j] = -0.5
                break


        print("starting value is "+str(i))
        print(modsequence)

# Input values
f = (x-3)*(x+3)*(x+20) # Example polynomial, change it to your desired polynomial
p = 3    # Example prime number, change it to your desired prime
n= 0  #example first value to check
r = 100   # Example range, determines how many values, starting at zero, to check sequences for
l = 14    # Example length, determines how large the generated sequences will be

generate_sequences(f,p,n,r,l)







