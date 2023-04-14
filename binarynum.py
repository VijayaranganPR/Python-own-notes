N = int(input())

n = N
l =[]
while(True):
    temp = n%2
    l.insert(0,str(temp))
    temp = n//2
    if n == 1:
        break
    n = temp
print("".join(l))