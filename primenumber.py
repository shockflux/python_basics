n=int(input("enter number to find the prime number"))
for i in range(2,n):
    j=2
    counter=0
    while(j<i):
        if(i%j==0):
            counter=1
            j=j+1
        else:
            j+=1
    if(counter==0):
        print(i,"\t is the prime number")
    else:
        counter=0