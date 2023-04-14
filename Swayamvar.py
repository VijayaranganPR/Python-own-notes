N = int(input())
bride = input()
groom = input()
temp1 = ''
temp2 = ''


while True:
    
    if len(bride)==0:
        break
    
    if (bride!=temp1 and groom!=temp2):
        
        if bride[0]==groom[0]:
            temp1 = bride
            temp2 = groom
            bride = bride[1:]
            groom = groom[1:]

        else:
            temp2 = groom
            groom = groom[1:] + groom[0]
    else:
        break
        
print(len(bride)) 