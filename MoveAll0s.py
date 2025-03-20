def pushZerosToEnd(a, a_size):
    zero=0
    nonzero=0
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero]=a[zero],a[nonzero]
            zero+=1
        nonzero+=1
a=[1,2,0,0,8,9,3,0,0,43,54]
a_size=len(a)
print(a)
pushZerosToEnd(a, a_size)
print("Array after pushing all zeros to end of array: ")
print(a)