n=int(input("enter a number : "))

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(0,i):
        print('*',end=" ")
    print()