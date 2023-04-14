def itrat(n):
    n=0
    temp=afad
    for i in range(len(str(afad))):
        last=temp%10
        n+=last**2
        temp=int(temp/10)
    return(n)
num=7
afad=num
print(afad)
afad=itrat(afad)
print(afad)
while (True):
    if afad==1:
        print('The given number is a happy number :',num)
        print(afad)
        break
    elif afad==4:
        print("The given number is not a happy number : ",num)
        break
    else:
        afad=itrat(afad)
        print(afad)