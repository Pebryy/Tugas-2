# Recursive factorial

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

print("Faktorial 5 =", faktorial(5))