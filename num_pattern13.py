n=int(input('enter a number : '))

for i in range(1,n+1):
    for j in range(1,i+1):
        for _ in range(3):
            print(j,end="")
        print(end=" ")
    print()