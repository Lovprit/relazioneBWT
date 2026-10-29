stringa = "banana"
print(stringa)
stringa = stringa + "$"
print(stringa)

lista = []

for i in stringa[:-1]:
    s = stringa[0]
    stringa = stringa[1:] + s
    lista.append(stringa) 
    print(stringa)
