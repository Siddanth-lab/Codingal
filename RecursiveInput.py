def getinput():
    num=int(input("Enter a number: "))
    if num<0:
        print("Negative number entered. Exiting...")
        return
    getinput()
getinput()