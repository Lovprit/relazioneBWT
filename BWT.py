stringa = "banana"
print(stringa)
stringa = stringa + "$"
print(stringa)

print("-------------------------------")
lista = []

for i in stringa:
    lista.append(stringa)
    print(stringa)
    s = stringa[0]
    stringa = stringa[1:] + s
    
    
print("-------------------------------")
for i in lista:
    print(i)

print("-------------------------------")

lista.sort()

for i in lista:
    print(i)

print("-------------------------------")
str_BWT = ""
c = 0
for i in lista:
    valore = lista[c]
    str_BWT = str_BWT + valore[-1]
    c = c + 1

print(str_BWT)