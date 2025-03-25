def maxSubArraySum(a, a_size):
    gmax = a[0]  
    cmax = 0  

    for i in range(a_size):
        cmax += a[i]
        if cmax > gmax:
            gmax = cmax
        if cmax < 0:
            cmax = 0  

    return gmax

a = [3, -4, 5, 3, 2, 4, 5, -22, -4, -25, 25, 2, -9]
b = [2, 3, 4 ,4 ,4 ,3, 3]
print(maxSubArraySum(a, len(a)))
print(maxSubArraySum(b, len(b)))