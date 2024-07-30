n=int(input("enter a number : "))
half=(n//2)+1
for i in range(0,half):
    for j in range(half-i-1):
        print('',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
n=n-half
for i in range(n,0,-1):
    for j in range(n-i+1):
        print('',end=" ")
    for j in range(i):
        print('*',end=" ")
    print()