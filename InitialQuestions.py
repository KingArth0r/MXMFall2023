import numpy as np
import sympy as sp

x = sp.symbols('x')

def generate_matrix_eigenvalues(f, p, n):
    # Define the variable and polynomial using SymPy

    polynomial = sp.Poly(f, x)

    # Calculate the size of the matrix
    matrix_size = p**n

    # Initialize a NumPy array with zeros
    matrix = np.zeros((matrix_size, matrix_size), dtype=int)

    # Fill the matrix based on the specified condition
    for i in range(matrix_size):
        for j in range(matrix_size):
            if (p*i - polynomial.subs(x, j)) == 0 or (p**n) % (p*i - polynomial.subs(x, j)) == 0:
                matrix[i, j] = 1

    # Calculate the eigenvalues of the matrix
    print(matrix)
    eigenvalues = np.linalg.eigvals(matrix)

    return np.max(eigenvalues)

# Input values
f = x**2 - x   # Example polynomial, change it to your desired polynomial
p = 2           # Example prime number, change it to your desired prime
n = 4         # Example integer value, change it to your desired integer

eigenvalue = generate_matrix_eigenvalues(f, p, n)
print("Lambda(f,p,n):", eigenvalue)




