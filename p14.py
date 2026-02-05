# Brute-forced it again. The code finds the solution in less than 10 seconds;
# I guess that's fine, although it must scale horribly. The answer is 837799.

def chain_count(n):  # counts the number l of links on a Collatz chain with starting value n
    l = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        l += 1
    return l

def long(max):  # returns the starting value x for the longest Collatz chain, where x <= max
    x = 1
    l_max = 1  # largest found length of a Collatz chain, currently
    for i in range(1, max + 1):
        if chain_count(i) > l_max:
            l_max = chain_count(i)
            x = i
    return x


print(long(10**6))