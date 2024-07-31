# n=int(input("enter a number : "))
word=(input("enter a string : "))
n=len(word)
for i in range(n):
    for j in range(i+1):
        print(word[j],end=" ")
    print()