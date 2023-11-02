import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spsl
from collections import defaultdict

def generate_matrix(f, p, n):
    matrix_size = p**n
    #lil_matrix = sps.lil_matrix((matrix_size, matrix_size), dtype=np.float64)

    # Rule: M[i,j] = 1 if p^n | p*i - f(j), 0 otherwise
    # Algorithm: a_ij = 1 iff i = f(j)/p mod p^(n-1)

    jtable = defaultdict(list)
    for j in range(1, matrix_size + 1):  # Start index from 1
        jtable[(np.polyval(f, j) / p) % (p ** (n - 1))].append(j)

    lil_matrix = sps.lil_matrix((p ** (n - 1), matrix_size), dtype=np.float32)
    for i in range(1, p ** (n - 1) + 1):  # Start index from 1
        for j in jtable[i % p ** (n - 1)]:
            lil_matrix[i - 1, j - 1] = 1.0  # Adjust indices by subtracting
    #Stack repeating pattern after doing the first p rows
    return sps.vstack([lil_matrix] * p).tocsr()

def largest_eigenvalue(matrix):
    # We return the real part since we know the actual result must be real
    eigenvalue, _ = spsl.eigs(matrix, k=1, which='LR')
    return eigenvalue[0].real
