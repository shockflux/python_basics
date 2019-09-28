#product of number in a list

#to take numbers in list from user
l=[]
n=int(input("enter limit of the list"))
for i in range(n):
    ele=int(input("enter element in the list"))
    l.append(ele)

product=1
for prod in l:
    product=product*prod
print("the product is",product)
