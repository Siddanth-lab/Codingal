def leaders(a,a_size):
    currentmax=a[a_size-1]
    print(currentmax)

    for i in range(a_size-2,-1,-1):
        if currentmax<a[i]:
            print(a[i])
            currentmax=a[i]
a=[34,12,4,6,5,243]
leaders(a,len(a))
