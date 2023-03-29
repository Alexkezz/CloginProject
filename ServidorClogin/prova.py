a = []

archivo = open("basedades.txt", "a")
archivo.write(",alex:123")
archivo.close()

archivo2 = open("basedades.txt", "r")
s = archivo2.read()
print(s.split(","))
a = s.split(",")
archivo2.close()
print(a)