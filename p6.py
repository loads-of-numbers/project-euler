# Almost a one-liner. Just uses the fact that 1 + 2 + ... + n = n(n+1)/2 and 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6.
# The answer is 25164150.

def diff(n):
    return ((n**2) * ((n+1)**2))//4 - (n*(n+1)*((2*n) + 1))//6


print(diff(100))
