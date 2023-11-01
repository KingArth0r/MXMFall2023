from Sparse import *
import matplotlib.pyplot as plt
import time

# Choose a prime p, and a natural number n < 10 and the degree of the polynomials you wish to investigate
# Also enter the number of polynomials you wish to generate
# This program will generate random monic polynomials up to the given degree with coefficients between -p^n and p^n
# and plot the largest eigenvalues and plot a heatmap for the nonzero elements of the generated matrices
# This program will also print out the coefficients of polynomials in which it encountered an error
# As of now the reason for the error is unknown since it's an open bug in the ARPACK library
p = 3
n = 5
degree = 5
num_polynomials = 500

def display_matrix(matrix):
    fig = plt.figure(1)
    dense_matrix = matrix.toarray()
    plt.imshow(dense_matrix, cmap='hot', interpolation='nearest')

def display_eigenvalues(eigenvalues):
    fig = plt.figure(2)
    plt.scatter(list(range(len(eigenvalues))), eigenvalues)

start_time = time.time()
total_matrix = sps.csr_matrix((p**n, p**n))
eigenvalues = []
for _ in range(num_polynomials):
    f_coefficients = np.random.randint(-p**n, p**n, degree + 1)
    f_coefficients[0] = 1
    f = np.poly1d(f_coefficients)
    matrix = generate_matrix(f, p, n)
    try:
        eigenvalue = largest_eigenvalue(matrix)
        eigenvalues.append(eigenvalue)
    except:
        print(f_coefficients)
    total_matrix += matrix
display_matrix(total_matrix)
display_eigenvalues(eigenvalues)
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime}")
plt.show()