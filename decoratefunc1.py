#decorate string 
def decor(fun):
    def inner(n):
        result=fun(n)
        result+=" how are you"
        return result
    return inner
@decor
def num(name):
    return "hello "+name
print(num("hi"))