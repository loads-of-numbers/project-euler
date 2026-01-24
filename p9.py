# By running the program, we find out (a,b,c) = (200,375,425) is the solution.
# I arrived at 10^6 - 2*10^3(a+b) + 2ab = 0 working with the system below:
# a^2 + b^2 = c^2 (I)
# a + b + c = 1000 (II)

def main():
    a = 1
    b = 1
    while a < 10**3:
        while b < 10**3:
            if 10**6 - 2*(10**3)*(a+b) + 2*a*b == 0:
                val = a*b*(10**3 - (a+b))
                print("Yes: (a,b,c) =", (a, b, (10**3 - (a+b))), "-- abc =", val)
                break
            else:
                print("No: (a,b) =", (a, b))
                b += 1
        if 10**6 - 2*(10**3)*(a+b) + 2*a*b == 0:
            break
        a += 1
        b = 0


main()
