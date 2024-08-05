n=int(input("Enter a number : "))

for i in range(n+1): #8
    for j in range(13):
        if (i==2 or i==6) or (i+j==6) or (j-i==6) or (i-j==2) or (i+j==14):
            print("*",end="")
        else:
            print(" ",end="")
    print()