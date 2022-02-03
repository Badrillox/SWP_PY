def addieren(a, b):
    return a+b

def addieren2(a,b=5):
    return a+b

def addieren3(a=3,b=5):
    return a+b

#def addieren(a, b, c):
#    return a+b+c

print(addieren(4, 5))
print(addieren2(5))
print(addieren2(5, 6))
print(addieren3(5, 6))


def summieren(*args):
    erg = 0
    for x in args:
        erg += x
    return erg

print(summieren(1, 2, 3))
print(summieren(1,2,3,4,5))