n=int(input("Enter a number : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print(i,end="")
        elif(i+j==n+1):
            print(j,end="")
        else:
            print(end=" ")
    print()