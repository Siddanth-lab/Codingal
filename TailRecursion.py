def tailrec(n, num):
    if n>num:
        return
    tailrec(n+1, num)
    print(n)
n=int(input("Enter n to print 1 to n: "))
tailrec(1,n)