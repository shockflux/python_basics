#to display odd number from user input
x=int(input("Enter X minimum number:"))
y=int(input("Enter Y maximum number:"))
if(x<y):
    while(x<=y):
        if(x%2!=0):
            print(x)
        x+=1
else:
    print("X should be smaller then Y")