a = input("Podaj pierwsza liczbe: ")
b = input("Podaj druga liczbe: ")
c = input("Podaj operator: ")
try:
    a = float(a)
    b = float(b)
except ValueError:
    print("To nie sa liczby!")

if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "/":
    print(a / b)
if c == "*":
    print(a * b)

