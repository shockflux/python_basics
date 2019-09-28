#assert condition
''' If the condition is true,
it does nothing and your program just continues to execute.
But if the assert condition evaluates to false,
it raises an AssertionError exception with an optional error message.'''

x=int(input("enter number greater than 10:"))
assert x>10 , "invalid number"
print("you entered",x)