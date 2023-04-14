n = int(input())
a = 0
b = 1
print(f"{a} {b} ", end = "")
for i in range(n-2):
    a,b = b,a+b
    print(b , end = " ")