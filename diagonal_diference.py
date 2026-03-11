def diagonalDifference(arr):
    # Write your code here
    return abs(sum(arr[_][_] for _ in range(len(arr))) - sum(arr[_][len(arr) - _ - 1] for _ in range(len(arr))))

mtrx = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(mtrx))
