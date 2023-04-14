 
for n in range(1,50):
    i = 8
    if n == 4 or n== 5:
        print("Facing away",n)
        continue
    c = 1
    while(i<=n):
        c+=1
        if c == 2:
            c = 0
        if i==n and c == 0:
            print("Facing each other",n)
            break
        if i == n and c == 1:
            print("Facing away",n)
            break

        i+=1
        if i==n and c == 0:
            print("Facing each other",n)
            break
        if i == n and c == 1:
            print("Facing away",n)
            break
        
        i+=3
        if i==n and c == 0:
            print("Facing each other",n)
            break
        if i == n and c == 1:
            print("Facing away",n)
            break

        i+=1
        if i==n and c == 0:
            print("Facing each other",n)
            break
        if i == n and c == 1:
            print("Facing away",n)
            break

        i+=3
    else:
        print("Independent",n)