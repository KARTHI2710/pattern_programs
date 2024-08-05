n=int(input('Enter a number : '))
start=0

for i in range(1,n+1):
    start+=i

for i in range(1,n+1):
    val=start
    for j in range(1,i+1):
        print(val,end=" ")
        dec=n-j
        val=val-dec
    start=start-1
    print()