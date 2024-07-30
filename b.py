for i in range(0,7):
    for j in range(0,5):
        if ((i==0 or i==3 or i==6) and j!=4) or ((i==1 or i==2 or i==4 or i==5) and (j==0 or j==4)):
            print('*',end="")
        else:
            print(' ',end="")
    print()