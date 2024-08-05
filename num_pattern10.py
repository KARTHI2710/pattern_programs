n=(input("Enter a number : "))

for i in range(0,len(n)):
    for j in range(0,len(n)):
        if(i==j or i+j==len(n)-1):
            print(n[i],end="")
        else:
            print(end=" ")
    print()