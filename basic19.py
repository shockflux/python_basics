#factorial of n number usinf recursion
def fact(n):
    if(n==0):
        return 1
    else:
        return n* fact(n-1)
#main program
n=int(input("Enter number to find factorial:"))
print(fact(n))