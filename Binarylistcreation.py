N = int(input())

for i in range(1,N+1):
    n = i
    l =[]
    while(True):
        temp = n%2
        l.insert(0,str(temp))
        
        temp = n//2
        if n == 1:
            break
        n = temp
    print('{0:>7} - {1:>7}'.format(i,"".join(l)))