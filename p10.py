# Sums the desired value while performing the sieve of Eratosthenes. The answer is 142913828922.

def prime_sum(n):
    lst = [True] * (n+1)
    lst[0] = lst[1] = False

    val = 0
    for i in range(2, n+1):
        if lst[i]:
            val += i
            for j in range(i**2, n+1, i):
                lst[j] = False

    return val


print(prime_sum(2 * (10 ** 6)))
