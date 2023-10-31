import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spsl
from collections import defaultdict
import time

def generate_matrix(f, p, n):
    matrix_size = p**n
    lil_matrix = sps.lil_matrix((matrix_size, matrix_size), dtype=np.float64)

    #Bug: It seems that the largest eigenvalue is just p.

    #Rule: M[i,j] = 1 if p^n | p*i - f(j), 0 otherwise
    #Algorithm: a_ij = 1 iff i = f(j)/p mod p^(n-1)


    jtable = defaultdict(list)
    for j in range(1, matrix_size + 1):  # Start index from 1
        jtable[(np.polyval(f, j) / p) % (p ** (n - 1))].append(j)

    for i in range(1, matrix_size + 1):  # Start index from 1
        for j in jtable[i % (p ** (n - 1))]:
            lil_matrix[i - 1, j - 1] = 1.0  # Adjust indices by subtracting

    return lil_matrix.tocsr()

def largest_eigenvalue(matrix):
    eigenvalue, _ = spsl.eigs(matrix, k=1, which='LR')  # Get the largest real part eigenvalue
    print(eigenvalue)
    return eigenvalue[0].real

def main():
    # Input values
    p = 2           # Example prime number, change it to your desired prime
    n = 3           # Example integer value, change it to your desired integer

    # Generate the matrix using a numpy polynomial
    f_coefficients = [1, 0, 1, 0]  # Coefficients for f
    f = np.poly1d(f_coefficients)
    start_time = time.time()
    matrix = generate_matrix(f, p, n)


    # Calculate the largest eigenvalue
    largest_eig = largest_eigenvalue(matrix)
    end_time = time.time()
    runtime = end_time - start_time

    print("Largest Eigenvalue:", largest_eig)
    print(f"Runtime: {runtime}")

if __name__ == "__main__":
    main()