def permuta(c):
    if len(c) == 0: return [[]]
    lst = []
    for i in permuta(c[1:]):
        lst = lst + multiple(c[0], i)
    return lst

def inserta(n, lst, i):
    return lst[:i] + [n] + lst[i:]

def multiple(n, lst):
    return [inserta(n, lst, i) for i in range(len(lst) + 1)]

if __name__ == '__main__':
    lista = [1,2,3]
    print(permuta(lista))
