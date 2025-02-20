def headrec(n,num):
    if n>num:
        return
    print(n)
    headrec(n+1,num)
n=int(input("Enter n to print 1 to n: "))
headrec(1,n)