def euclid(a,b):
    if a%b == 0:
        return b
    return euclid(b, a%b)

euclid(18,12)
