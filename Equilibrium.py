def equilibriumPoint(arr):
    leftsideSum=0
    rightsideSum=0
    n=len(arr)

    for i in range(n):
        leftSideSum=0
        rightSideSum=0

        for j in range(i):
            leftSideSum +=arr[j]
        
        for j in range(i+1,n):
            rightSideSum+=arr[j]
        
        if leftSideSum==rightSideSum:
            return i
    return -1
arr=[-2,6,2,0,0,3,4]
print("Element: ", arr[equilibriumPoint(arr)])