# I don't know if there's a better way to do this, but I guess it isn't that bad.
# Throughout the code, there are snippets explaining how it works. The answer is 21124.

def letter_count(n):  # counts the letters of n, when written out in words, where n < 1000
    n = str(n)
    n = '0'*(3-len(n)) + n  # formats every number to a string of 3 digits
    l = 0  # number of letters
    units = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}  # 0-9
    ten = {0:3, 1:6, 2:6, 3:8, 4:8, 5:7, 6:7, 7:9, 8:8, 9:8}  # 10-19
    tens = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}  # 20, 30, ..., 90
    (a,b,c) = (int(n[0]),int(n[1]),int(n[2]))  # each digit of n
    if b == 1:
        l += ten[c]
    else:
        l += units[c] + tens[b]
    if a != 0:
        if (b,c) != (0,0):
            l += 10 + units[a]  # 'hundred and' is added here
        else:
            l += 7 + units[a]  # 'hundred' is added here
    return l


def loop(m):  # counts the letters of all numbers from 1 to m, m < 1000
    total = 0
    for i in range(1, m+1):
        total += letter_count(i)
    return total

print(loop(999) + 11)  # adds 'one thousand' manually