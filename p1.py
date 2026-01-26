# I'm sure there's no need for explanations.

def foo(n):  # sums multiples of 3 or 5 up to n
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
           sum += i

    return sum


print(foo(1000))
