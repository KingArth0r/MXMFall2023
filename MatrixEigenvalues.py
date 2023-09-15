import numpy as np
import sympy as sp
import time
import json

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

    return np.real(np.max(eigenvalues))

def main():
    checked_data = []

    # Initial settings
    primes = [2, 3, 5]  # List of primes to iterate through
    degrees = [1, 2, 3]         # Start with linear polynomial
    coefficient = 0       # Initialize the coefficient

    while True:
        for p in primes:
            for n in degrees:
                polynomial = x ** 2 + x + coefficient
                start_time = time.time()
                runtime = 0

                try:
                    eigenvalues = generate_matrix_eigenvalues(polynomial, p, n)
                    end_time = time.time()
                    runtime = end_time - start_time

                    result = {
                        "Prime": p,
                        "Degree": n,
                        "Coefficient": coefficient,
                        "Runtime": runtime,
                        "Eigenvalues": eigenvalues.tolist()
                    }

                    checked_data.append(result)
                    print(f"Prime: {p}, Degree: {n}, Coefficient: {coefficient}, Runtime: {runtime:.2f} seconds")

                except Exception as e:
                    print(f"Error: {e}")

                # Adjust parameters if either runtime exceeds 60 seconds
                if runtime > 60 or coefficient >= 100:
                    coefficient = 0
                    if n == 1:
                        primes.remove(p)
                        n = 0
                    else:
                        degrees.append(n - 1)
                else:
                    coefficient += 1


        # Check for termination condition
        if primes == [] or (n == 0 and coefficient == -n):
            break

        # Increment coefficient for the next iteration
        coefficient += 1

    # Save the checked data to a JSON file
    with open("checked.json", "w") as json_file:
        json.dump(checked_data, json_file, indent=2)

if __name__ == "__main__":
    main()