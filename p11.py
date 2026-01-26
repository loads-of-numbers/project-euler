# Horrible code, I know, but it gets the job done. Each "section" is a scan in a different direction
# (horizontally, vertically, on left diagonals and right diagonals). Originally, I wasn't sure if
# right diagonals were supposed to count; apparently, they do. If I had more patience, I would
# have shortened the redundant parts as to make it neatear. The answer is 70600674.
import numpy as np

def largest(arr):
    scan = []
    prod = 1
    dim = arr.shape

    for i in range(dim[0]):  # rows
        scan.extend([arr[i,0], arr[i,1], arr[i,2], arr[i,3]])
        for j in arr[i,4:]:
            prod2 = scan[0] * scan[1] * scan[2] * scan[3]
            if prod2 > prod:
                prod = prod2
            scan.pop(0)
            scan.append(j)

    scan = []
    for j in range(dim[1]):  # columns
        scan.extend([arr[0,j], arr[1,j], arr[2,j], arr[3,j]])
        for i in arr[4:,j]:
            prod2 = scan[0] * scan[1] * scan[2] * scan[3]
            if prod2 > prod:
                prod = prod2
            scan.pop(0)
            scan.append(i)

    scan = []
    for i in range(-dim[0]+4, dim[1]-3):  # left diagonals
        diag = np.diagonal(arr, i)
        scan.extend([diag[0], diag[1], diag[2], diag[3]])
        for j in diag[4:]:
            prod2 = scan[0] * scan[1] * scan[2] * scan[3]
            if prod2 > prod:
                prod = prod2
            scan.pop(0)
            scan.append(j)

    scan = []
    for i in range(-dim[0] + 4, dim[1] - 3):  # right diagonals
        diag = np.diagonal(np.fliplr(arr), i)
        scan.extend([diag[0], diag[1], diag[2], diag[3]])
        for j in diag[4:]:
            prod2 = scan[0] * scan[1] * scan[2] * scan[3]
            if prod2 > prod:
                prod = prod2
            scan.pop(0)
            scan.append(j)

    return prod

arr = np.loadtxt("p11_array.txt", dtype=int)
print(largest(arr))
