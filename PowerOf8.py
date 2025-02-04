def PowerOf8(n):
    if n<=0:
        return False
    while n% 8==0:
        n//=8
    return n==1
num=int(input("Enter a number: "))
if PowerOf8(num):
    print(f"{num} is a power of 8.")
else:
    print(f"{num} is not a powerof 8.")