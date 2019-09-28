#print from 1 to 20 but skip multiples of 3
x=1
while(x<21):
    x+=1
    if(x%3==0):
        continue
    print(x)