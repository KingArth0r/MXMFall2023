import numpy as np

def generate_sequences(f_coefficients, p, valuerange, length):
    polynomial = np.poly1d(f_coefficients)
    for i in range(valuerange):
        sequence = np.zeros(length)
        modsequence = np.zeros(length)
        startingvalue = i
        sequence[0] = startingvalue
        try:
            for j in range(1, length):
                check = (polynomial(sequence[j - 1]) / p)
                if check.is_integer() and check < float('inf'):
                    sequence[j] = (polynomial(sequence[j - 1]) / p)
                else:
                    sequence[j] = np.nan
                    break

            modsequence = np.mod(sequence, p)

            print("Starting value is " + str(i))
            print(sequence)
            print(modsequence)
        except Exception as e:
            print("Error:", e)

# Input values
f_coefficients = [1, -1, 0]  # Coefficients for x^2 - x (example polynomial)
p = 3                        # Example prime number
r = 10                       # Example range
l = 20                       # Example length

generate_sequences(f_coefficients, p, r, l)
