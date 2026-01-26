# Quite intuitive.

def fib(n):  # sums even-valued fibonacci numbers less than n
    sum = 0
    f0 = 1
    f1 = 2
    f2 = 2
    while f2 <= n:
        if f2 % 2 == 0:
            sum += f2
        f2 += f0
        f0 = f1
        f1 = f2

    return sum


print(fib(4*(10**6)))
