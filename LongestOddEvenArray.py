def longestAltSubArray(arr):
    if not arr:
        return 0
    
    MaxLength=1
    CurrentLength=1

    for i in range(1,len(arr)):
        if(arr[i]%2==0 and arr[i-1]%2 !=0) or (arr[i]%2 !=0 and arr[i-1]%2==0):
            current_length+=1
            MaxLength=max(MaxLength, CurrentLength)
        else:
            current_length=1
        return MaxLength
    arr=[1,2,3,4,5,6,7,8,9,10]
    print("Longest Alt odd-even subarray length: ", longestAltSubArray(arr))