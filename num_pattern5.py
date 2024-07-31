n=int(input("Enter a number : "))

for i in range(1,n+1):
    val=i
    dec=n-1
    for j in range(1,i+1):
        print(val,end=" ")
        val=val+dec
        dec-=1

    print()