C = int(input())
d = {}
for _ in range(C):
    L = input().split()
    D = input().split()
    for i in range(1,int(L[0])+1):
        if L[i] in d:
            d[L[i]] += 1
        else:
            d[L[i]] = 1
    for j in range(1,int(D[0])+1):
        if D[j] in d:
            d[D[j]] -= 1
        else:
            d[D[j]] = -1
result = []
for i in d:
    if d[i] >0:
        result.append(i)
print(f"{len(result)} {' '.join(result)}")