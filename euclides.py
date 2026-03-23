def euler(n):
    cont = 0
    for k in range(1, n):
        if euclid(n,k)==1:
            cont += 1
    return cont
            

def euclid(a,b):
    if a%b == 0:
        return b
    return euclid(b, a%b)

print(euclid(18,12))
print(euler(12))
