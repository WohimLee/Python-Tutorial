

a = [1, 2, 3]
b = a

print(b is a)
print(a == b)

b = a[:]
print(id(a))
print(id(b))
print(b is a)
print(b == a)