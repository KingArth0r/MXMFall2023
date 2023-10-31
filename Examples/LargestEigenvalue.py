from Sparse import *

# This program will print the largest eigenvalue and runtime for a given prime p and number n.
# The complexity is O(p^n) so increasing n by 1 will increase time by a factor of p
# The coefficients are from highest degree to lowest (including constant)
# Example: x^3 + x is represented with [1, 0, 1, 0] and x^4 + 2x^2 - 5 is [1, 0, 2, 0, -5]
# You can change the number of elements in the array to change the degree.
p = 3
n = 7
f_coefficients = [1, 0, 1, 0]


f = np.poly1d(f_coefficients)
start_time = time.time()
matrix = generate_matrix(f, p, n)

# Calculate the largest eigenvalue
largest_eig = largest_eigenvalue(matrix)
end_time = time.time()
runtime = end_time - start_time

print("Largest Eigenvalue:", largest_eig)
print(f"Runtime: {runtime}")