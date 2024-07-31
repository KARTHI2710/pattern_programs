n=int(input('Enter a number : '))
m=n
for i in range(0,n):
    for j in range(n-i):
        print(m,end=" ")
    m-=1
    print()