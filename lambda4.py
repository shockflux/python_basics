#filter even and odd numbers from a list using filter and lambda
l=[1,2,3,4,5]
result=filter(lambda x:x%2==0,l) #it will print the memory location of the function to print numbers convert it in to list
print(result)
result1=list(filter(lambda x:x%2==0,l))#converted into list
print(result1)