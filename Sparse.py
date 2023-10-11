import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spsl

def generate_matrix(f, p, n):
    matrix_size = p**n
    lil_matrix = sps.lil_matrix((matrix_size, matrix_size), dtype=np.float64)

    for i in range(1, matrix_size + 1):
        for j in range(1, matrix_size + 1):
            if p*(i) - np.polyval(f,j) == 0 or (p**n) % (p*i - np.polyval(f, j)) == 0:
                lil_matrix[i - 1, j - 1] = 1.0

    return lil_matrix.tocsr()

def largest_eigenvalue(matrix):
    eigenvalue, _ = spsl.eigs(matrix, k=1, which='LR')  # Get the largest real part eigenvalue
    return eigenvalue[0].real

def main():
    # Input values
    p = 5           # Example prime number, change it to your desired prime
    n = 4           # Example integer value, change it to your desired integer

    # Generate the matrix using a numpy polynomial
    f_coefficients = [1, 0, -2]  # Coefficients for x^2 - 2
    f = np.poly1d(f_coefficients)

    matrix = generate_matrix(f, p, n)
    print(matrix)

    # Calculate the largest eigenvalue
    largest_eig = largest_eigenvalue(matrix)

    print("Largest Eigenvalue:", largest_eig)

if __name__ == "__main__":
    main()