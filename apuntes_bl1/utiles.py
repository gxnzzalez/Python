# DEVUELVE COMO RESULTADO la suma de valores de una lista
def sumaLista(lista):
    suma = 0
    for x in lista:
        suma += x   # suma = suma + x
    return suma

# DEVUELVE COMO RESULTADO la media USANDO LA FUNCIÓN sumaLista 
def media(lista):
    media = sumaLista(lista)/len(lista)
    return media