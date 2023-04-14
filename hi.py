list1=[]
#s=int(input('Enter the starting limit: '))
#e=int(input('Enter the ending limit: '))
s=2
e=1000
for i in range(s,e+1):
    if (i==2)|(i==3)|(i==5)|(i==7):
            list1.append(i)
            continue
    elif i%2!=0:
        if(i%3!=0)&(i%5!=0)&(i%7!=0):
            list1.append(i)

print(list1)