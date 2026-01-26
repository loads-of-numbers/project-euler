# I'm proud of this. To compute the divisors of each triangular number t, it factors t into prime powers,
# then uses the divisor function d: since d(p^k) = k + 1 (where p^k is a prime power) and d is multiplicative,
# the number of divisors is calculated as quite a simple product in div_num(). It also calculates a table of
# primes using the sieve of Eratosthenes, as previously seen in problem 10. The answer to this one is 76576500.

def prime_table(n): # returns a set with all primes up to n
    lst = [True] * (n + 1)
    lst[0] = lst[1] = False
    tbl = set()

    for i in range(2, n+1):
        if lst[i]:
            tbl.add(i)
            for j in range(i**2, n+1, i):
                lst[j] = False

    return tbl

def prime_fact(n, tbl):  # returns the prime factorization of n as a set of tuples (p,k)
    fct = set()

    for p in tbl:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        fct.add((p,k))

    return fct

def div_num(n, tbl):  # returns the number of divisors of n
    prm = prime_fact(n, tbl)
    div = 1
    for tp in prm:
        div *= tp[1] + 1

    return div

def tri_num(lim):  # returns the smallest triangular number with at least lim divisors
    k = 1
    nat = 1
    tbl = prime_table(lim)
    
    while div_num(k, tbl) <= lim:
        nat += 1
        k += nat

    return k


print(tri_num(500))
