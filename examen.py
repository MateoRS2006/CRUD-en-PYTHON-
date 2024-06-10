def valor(n):
    tmp = 1
    for i in range(n):
        tmp*=i+1
    return tmp

print(valor(4))