n=int(input("Enter a Number : "))

for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i+1):
        if (j%2==0):
            print("*",end="")
        else:
            print("A",end="")
    print()