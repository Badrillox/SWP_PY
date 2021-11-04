a = [1, 2, 3] #list
b = (1, 2, 3) #tuple
c = True
d = False
e = None
import array
array.array("i", [1,2,3])
for element in a:
    print(element)
for i in range(6):
    print(i)
for i in range(5,11):
    print(i)
for i in range(5,11,2):
    print(i)
"""
for i in range(0, 10):
    if i % 2:
        print(i)
    else:
        print("schlecht")
"""
def addition(a,b):
    return a+b
print(addition(2,3))