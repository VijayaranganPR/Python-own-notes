a = input()
t = ''
for i in range(0,len(a)):
    if a[i].isdigit():
        t = t+a[i]
    elif a[i].isalpha():
        print(a[i]*int(t), end = "")
        t = ""