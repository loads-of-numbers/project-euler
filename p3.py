# I got stuck for quite some time trying to use the sieve of Eratosthenes when, in fact, the dumbest
# solution was the better one. The answer is 6857.

def lpd(n):  # finds the largest prime divisor (lpd) of n by prime factorization
    lpd = 1
    i = 2
    while i <= n:
        while n % i == 0:
            n /= i
        lpd = i
        i += 1
    return lpd


n = 600851475143
print(lpd(n))
