# El nombre del módulo a importar es el nombre del fichero
# Se importan las funciones que use del móudlo
from utiles import sumaLista, media

ventas = [1,2,3,4,5]
ventasTotales = sumaLista(ventas)

print("Lista ventas:", ventas)
print("Suma Ventas:", ventasTotales)