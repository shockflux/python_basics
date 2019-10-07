#returning multiple values
def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    g=a/b
    return x,y,z,g
#main program
result=calc(10,20)
print(result)