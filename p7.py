# I lazily repurposed prime_table() from Problem 12 to get a table of primes up to n. Since the prime number
# theorem states that π(N) ~ N/log(N), where π is the prime-counting function, I solved N/log(N) = 10002 with
# WolframAlpha and found out N ≈ 116697 < 120000. Then, I just called prime_table(120000) and hoped that it
# already had found the 100001st prime. Indeed, it had; the answer is 104743.

def prime_table(n): # returns a set with all primes up to n
    lst = [True] * (n + 1)
    lst[0] = lst[1] = False
    tbl = []

    for i in range(2, n+1):
        if lst[i]:
            tbl.append(i)
            for j in range(i**2, n+1, i):
                lst[j] = False

    return tbl


print(prime_table(120000)[10000])  # estimated from the prime number theorem
