#to generate custom numbers
def gen(x,y):
    while(x<y):
        yield x #yeild store the value
        x+=1
result=gen(11,21)
#print(list(result)) (run this if you want to know what yield actually does
for i in result:
    print(i)


