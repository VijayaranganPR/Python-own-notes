def phil(N):
    coin = 0
    while N >= 1:
        N = N // 2
        coin = coin + 1
    return coin
T=int(input())
l=[]
for i in range(0,T):
    N=int(input())
    l.append(phil(N))
for x in l:
    print(x)