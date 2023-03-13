a = b = c = "Python 2023"

print(a == b)
print(b == c)

print(type(a))
print( "\t" + hex(id(a)))
print(type(b))
print( "\t" + hex(id(b)))
print(type(c))
print( "\t" + hex(id(c)))

print("\n")
c = "Java 11"

print(a == b)
print(b == c)

print(type(a))
print( "\t" + hex(id(a)))
print(type(b))
print( "\t" + hex(id(b)))
print(type(c))
print( "\t" + hex(id(c)))