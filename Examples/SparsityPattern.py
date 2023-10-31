from Sparse import *
import matplotlib.pyplot as plt

# Choose a prime p, and a natural number n < 10 and the degree of the polynomials you wish to investigate
# This program will generate random monic polynomials up to the given degree with coefficients between -p^n and p^n
# and plot the largest eigenvalues and plot a heatmap for the nonzero elements of the generated matrices
p = 5
n = 4
degree = 5

def display_matrix(matrix):
    fig = plt.figure(1)
    dense_matrix = matrix.toarray()
    plt.imshow(dense_matrix, cmap='hot', interpolation='nearest')

def display_eigenvalues(eigenvalues):
    fig = plt.figure(2)
    plt.scatter(list(range(len(eigenvalues))), eigenvalues)


total_matrix = sps.csr_matrix((p**n, p**n))
eigenvalues = []
for _ in range(1000):
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
plt.show()