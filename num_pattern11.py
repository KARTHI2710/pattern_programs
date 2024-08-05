n=(input("Enter a number : "))

for i in range(0,len(n)):
    for j in range(0,len(n)):
        if(i==j):
            print(n[i],end="")
        elif(i+j==len(n)-1):
            print(n[j],end="")
        else:
            print(end=" ")
    print()