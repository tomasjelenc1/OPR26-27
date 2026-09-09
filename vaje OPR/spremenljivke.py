print("Hello world")

# integer - celo število
x = 10
y = -10

# operacija inta
print(x+y)
print(x-y)
print(x/y)
print(x*y)

#celoštevilsko deljenje
print(x//y)
print(int(x/y))

# deljenje z ostankom
print(x%2)

#preveriš kateri tip spremenljivke je
print(type(x))

#spreminjanje tipa (parse)
x = "12"
x = int(x)
print(x+1)

#string
a = "abc"
b = "def"

print(a+b)

#indeksiranje
print(a[0])

#rezine/slice
print(a[0:1])
print(a[::-1]) #obrnjen string

#f-string
ime = "Anja"
print("Pozdravljen {ime}")