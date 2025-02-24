def MaxElementArray(a):
    length=len(a)
    if length==1:
        return a[0]
    return max(a[0],MaxElementArray(a[1:]))
a=[2,354,83,92,173,2376]

print("Largest element of array: ",MaxElementArray(a))