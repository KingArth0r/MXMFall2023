# MXMFall2023
Programs meant to aid research for MXM Fall 2023

# Setup
Make sure you have the latest version of python and have the relevant packages installed.

### Sparse.py / test_Sparse.py
Do not modify

### EigenvaluesSlow.py 
This is outdated but here for documentation purposes

### Examples/LargestEigenvalues.py
To test different polynomials, p values, or n values, change the values at the top of the file to suit your curiosity.
For polynomials, you will enter an array of coefficients which go from highest degree to lowest. 
For example, `x^3 + x` would be represented with `[1, 0, 1, 0]`.

Be careful running the program for large p or n values, it may slow your computer.

### Examples/SparsityPattern.py
Choose a prime p, and a natural number n < 10 and the degree of the polynomials you wish to investigate
This program will generate random monic polynomials up to the given degree with coefficients between -p^n and p^n
and plot the largest eigenvalues and plot a heatmap for the nonzero elements of the generated matrices

### Examples/GeneratePictures.py
Instead of choosing just a singular prime, you can now make a list of primes and corresponding list of n values for the
program to plot the eigenvalues of the number of random monic polynomials that you choose. You also choose the degree of
the polynomials you wish to investigate. The program will export the pictures the eigenvalue_pictures folder.
The format of the files is "d" then the degree you entered, then "p" and then the prime it tested, then "n" and then 
the value entered for n. This program will also print out the coefficients of polynomials in which it encounters an
error. 
