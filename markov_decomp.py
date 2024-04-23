import numpy as np
d = lambda f: [i * f[i] for i in range(1, len(f))]
def check(f, p, n, decomp):
    for c in decomp:
        if len(set([eval(f,  + j * p ** n, p ** (n + 1)) for j in range(p)])) != p:
            return False
    return True
def eval(f, x, m):
    y = 0
    for i in range(len(f)):
        y = (y * x + f[-1-i]) % m
    return y

def decomp(f, p, n):
    df = d(f)
    C = []
    for i in range(p ** n):
        if eval(df, i, p ** n) == 0:
            C.append(i)
    decomp = [c for c in range(p ** n) if c not in C and eval(f, c, p) == 0]
    while not check(f, p, n, decomp):
        print(n)
        decomp = [c + b * p ** n for c in decomp for b in range(p)]
        n += 1
    print(decomp)
    M = np.zeros((len(decomp), len(decomp)))
    for i, c in enumerate(decomp):
        vals = []
        for b in range(p):
            vals.append(eval(f, c + b * p ** n, p ** (n + 1)) / p + 1)
        for v in vals:
            try:
                j = decomp.index(v)
                M[j][i] = 1
            except Exception as error:
                print("Exception: ", type(error).__name__)
                continue
    return M

def main():
  print(decomp([1, -2, 1, 0], 3, 3))

if __name__ == '__main__':
  main()
