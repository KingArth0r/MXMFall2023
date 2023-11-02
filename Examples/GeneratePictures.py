from Sparse import *
import time
import numpy as np
import matplotlib.pyplot as plt

# Define arrays P and N
P = [2, 3, 5, 7, 11, 13, 17, 19, 23]
N = [5, 5, 4, 4, 3, 3, 3, 2, 2]
degree = 6
num_polynomials = 2000

total_runtime = 0  # Initialize total runtime

for i in range(len(P)):
    p = P[i]
    n = N[i]
    eigenvalues = []  # Initialize eigenvalues list for current p and n
    start_time = time.time()

    for _ in range(num_polynomials):
        f_coefficients = np.random.randint(-p ** n, p ** n, degree + 1)
        f_coefficients[0] = 1
        f = np.poly1d(f_coefficients)
        matrix = generate_matrix(f, p, n)
        try:
            eigenvalue = largest_eigenvalue(matrix)
            eigenvalues.append(eigenvalue)
        except:
            print(f"Coefficients: {f_coefficients}")

    end_time = time.time()
    runtime = end_time - start_time
    total_runtime += runtime

    # Save eigenvalues plot to file
    filename = f"../eigenvalue_pictures/d{degree}p{p}n{n}.png"
    plt.scatter(list(range(len(eigenvalues))), eigenvalues)
    plt.savefig(filename)
    plt.close()

    print(f"Eigenvalues for p={p}, n={n} saved to: {filename}")
    print(f"Runtime for p={p}, n={n}: {runtime} seconds")

print(f"Total Runtime: {total_runtime} seconds")