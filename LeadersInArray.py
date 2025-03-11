def rotation(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp

def printArray(a, a_size):
    for i in range(a_size):  
        print("%d" % a[i], end=" ")
    print()  

a = [12, 21, 13, 58, 3, 2, 35, 32365]
print("Original Array:")
printArray(a, len(a))

rotation(a, 2, len(a))  
print("Array after rotation:")
printArray(a, len(a))