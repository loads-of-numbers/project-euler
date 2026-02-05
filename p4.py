# Brute-force approach, but it works fine. The answer is 906609.

def is_pal(n):  # checks if n is palindromic
    n = str(n)
    for i in range(len(n)//2 + 1):
        if n[i] != n[-i-1]:
            return False
    return True

def iter_digits():  # finds largest palindrome among products of 3 digit numbers
    (a,b) = (100,100)
    larg = 1
    while a <= 999:
        while b <= 999:
            if is_pal(a*b) and a*b > larg:
                larg = a*b
            b += 1
        a += 1
        b = 100
    return larg


print(iter_digits())