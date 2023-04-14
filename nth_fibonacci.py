
# Python3 program to find n'th 
# fibonacci Number 
# Fn = {[(√5 + 1)/2] ^ n} / √5
 
def fibo(n):
    phi = (1 + 5**0.5) / 2
    
    a = (phi**(n-1) / 5**0.5)
    if a % 10 >0.5:
        return round(a)
    else:
        return int(a)
       
n = int(input())
 print(fibo(n))