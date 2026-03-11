import numpy as np

def sgn(b):
    a = b.copy()
    cont, n = 0, len(a)
    while True:
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                cont += 1
                i -= 1
                break
        if i == n-2: break
    if cont%2 == 0: return 1
    return -1

def det(a):
    n = len(a)
    s = range(n)
    t = permutaciones(s)
    d = 0
    for u in t:
        r = sgn(u)
        for i in range(n):
            r = r*a[i, u[i]]
        d += r
    return d

def permutaciones(nums):
    if len(nums) == 0: return [[]]
    lst = []
    for i in permutaciones(nums[1:]):
        lst = lst + inserta_multiple(nums[0], i)
    return lst

def inserta(n, lst, i):
    return lst[:i] + [n] + lst[i:]

def inserta_multiple(n, lst):
    return [inserta(n, lst, _) for _ in range(len(lst) + 1)]

if __name__ == '__main__':
    a = [[1,3,5], [4,6,1], [2,4,3]]
    a = np.array(a)
    print(np.linalg.det(a))
    print(det(a))
