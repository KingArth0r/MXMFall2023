import pytest
from Sparse import *

def test_generate_matrix1():
    # Rule: M[i,j] = 1 if p^n | p*i - f(j), 0 otherwise (indexing starts at 1 and ends at p^n)
    # For f = x^2 + x + 1, p = 3, n = 2 the matrix should be
    # 1 0 0 1 0 0 1 0 0
    # 0 0 0 0 0 0 0 0 0
    # 0 0 0 0 0 0 0 0 0
    # 1 0 0 1 0 0 1 0 0
    # 0 0 0 0 0 0 0 0 0
    # 0 0 0 0 0 0 0 0 0
    # 1 0 0 1 0 0 1 0 0
    # 0 0 0 0 0 0 0 0 0
    # 0 0 0 0 0 0 0 0 0

    p = 3
    n = 2
    f_coefficients = [1, 1, 1]  # Coefficients for f
    f = np.poly1d(f_coefficients)

    matrix_size = p ** n
    lil_matrix = sps.lil_matrix((matrix_size, matrix_size), dtype=np.float64)
    for i in range(3):
        for j in range(3):
            lil_matrix[3*i,3*j] = 1.0

    assert (lil_matrix.tocsr() != generate_matrix(f, p, n)).nnz == 0

def test_generate_matrix2():
    #Rule: M[i,j] = 1 if p^n | p*i - f(j), 0 otherwise (indexing starts at 1 and ends at p^n)
    #The matrix should be
    # [1, 1, 0, 0, 1, 0, 0, 0]
    # [0, 0, 0, 1, 0, 0, 0, 0]
    # [0, 0, 1, 0, 0, 1, 1, 0]
    # [0, 0, 0, 0, 0, 0, 0, 1]
    # [1, 1, 0, 0, 1, 0, 0, 0]
    # [0, 0, 0, 1, 0, 0, 0, 0]
    # [0, 0, 1, 0, 0, 1, 1, 0]
    # [0, 0, 0, 0, 0, 0, 0, 1]
    p = 2
    n = 3
    f_coefficients = [1, 0, 1, 0]  # Coefficients for f
    f = np.poly1d(f_coefficients)
    lil_matrix = sps.lil_matrix([[1, 1, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 1, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1]])
    assert (lil_matrix.tocsr() != generate_matrix(f, p, n)).nnz == 0



