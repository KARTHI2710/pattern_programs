n=int(input('Enter a number : '))

for i in range(0,n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()