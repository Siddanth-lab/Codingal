numberLargest=int(input("Enter the Largest number : "))
numberSmallest=int(input("Enter the smallest number : "))

while (numberSmallest):
    numberStore=numberSmallest
    numberSmallest=numberLargest%numberSmallest
    numberLargest=numberStore

print('HCF is : ', numberLargest)
