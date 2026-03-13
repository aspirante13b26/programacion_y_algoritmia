def conver_base(n, b):
    if n < b: return [n]
    return rb(n//b, b) + [n%b]


def conver_base__iter(n,b):
    c = []
    while n >= b:
        c.append(n%b)
        n = n//b
    c.append(n)
    return c


def Hornet(a, x):
    # a = [a_0, a_1, a_2, ...]
    if a == []: return 0
    return Hornet(a[1:], x)*x + a[0]


def eval_poli(a, x):
    p = 1; r = 0
    for i in range(len(a)):
        r = r + a[i]*p
        p = p*x
    return r

if __name__ == '__main__':

    print(conver_base(11, 2))
    print(conver_base__iter(11,2))
    coef = [3,0,2,1]
    base = 2
    print(Hornet(coef, base))
    print(eval_poli(coef, base))
