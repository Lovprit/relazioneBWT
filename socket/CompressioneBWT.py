def BWT(stringa):
    stringa = stringa + "$"

    lista = []

    for i in stringa:
        lista.append(stringa)
        s = stringa[0]
        stringa = stringa[1:] + s


    lista.sort()

    for i in lista:
        print(i)

    print("Compressione BWT")
    str_BWT = ""
    c = 0
    for i in lista:
        valore = lista[c]
        str_BWT = str_BWT + valore[-1]
        c = c + 1
    return str_BWT

