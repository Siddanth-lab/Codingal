weather=(1,0,0,0,1,1,0)
sunny=0
rainy=1
for i in range(0,7):
    if(weather[i]==0):
        rainy+1
    else:
        sunny+1
if (sunny>rainy):
    print("Good Weather")
else:
    print("Bad Weather")
        