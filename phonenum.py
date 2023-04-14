phone = {}
l=[]
n = int(input())
for i in range(n):
    a = input().split()
    phone[a[0]] =int(a[1])
while (True):
    try:
        ask = input()
    except:
        break
    if ask not in phone.keys():
        l.append('Not found')
    else:
        l.append(f'{ask}={phone[ask]}')
for i in l:
    print(i)
