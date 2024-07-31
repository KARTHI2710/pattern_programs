n=int(input("Enter a number : "))

for i in range(0,n):
    for j in range(0,2*n-1):
        if (i==n-1 and j%2==0) or (i+j==n-1) or (j-i==n-1):
            print('*',end="")
        else:
            print(end=" ")
    print()