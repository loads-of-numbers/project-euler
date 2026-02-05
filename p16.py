# That was surprisingly easy.
# The answer is 1366.

def digit_sum(n):  # returns the sum of the digits of n
    sum = 0
    n = str(n)
    for i in n:
        sum += int(i)
    return sum


print(digit_sum(2**1000))