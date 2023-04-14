

P = int(input()) # minimum length
Q = int(input()) # maximum length
R = int(input()) # minimum width
S = int(input()) # maximum width
std=0

temp1=P


l = []
while(temp1<=Q):
    
    temp2=R
    while (temp2<=S):
        l.append([temp1,temp2])
        temp2+=1
    temp1+=1
    

for ind in range(len(l)):
    
    while (l[ind][0]!=l[ind][1]):
        ma = l[ind].index(max(l[ind]))
        l[ind][ma] = max(l[ind]) - min(l[ind])
        
        std+=1
        
        
    else:
        
        std+=1
        
print(std)