#function as parameter to another
def display(fun):
    return "hello" + '\t' + fun

def name():
    return"shockflux"

print(display(name()))