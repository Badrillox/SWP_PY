def test(a,b):
    return a,b

test(1, 2)

def test2(a,b = 5):
    pass
test2(5, 2)
test2(5)

def test3(a=5, b=3):
    pass
print(test3())
test3(5, 5)
test3(a=10, b=10)
test3(b=12)
test3(b=12, a=14)

l = [1,2,3, 4, 5, 6, 7]

l.append(8)
print(l)
len(l)
l.pop()
max(l)
l.count(2)