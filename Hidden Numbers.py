for T in range(int(input())):
    N=int(input())
    flag=False
    for a in range(1,10):
        for b in range(1,10):
            if a*b==N:
                print(a,b)
                flag=True
        if flag==True:
            break