#sum of elemnts in list using reduce and lambda function
from functools import reduce
l=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,l)
print(result)