import funciones as f

lista = f.obtener_productos() #usando la API
# #lista = LISTA_dummy  #si no usa la API

# print(lista)


#Ejercicio mostrar lista
# f.mostrar_productos(lista)

# #Ejercicio busca por titulo
# titulo = input("Titulo del producto a encontrar:")
# encontrar = f.buscar_por_titulo(lista, titulo)
# f.mostrar_productos(encontrar)

#Ejercicio filtros

filtrado = f.filtrar_productos(lista, None, None, True)
f.mostrar_productos(filtrado)

#EJERCICIO MENU INTENTO
# categoria = input("Categoria del producto(beauty, fragances):")
# maximo = int(input("Precio maximo del producto:"))
# disponibilidad = bool(input("Disponibilidad:"))
# filtrar = f.filtrar_productos(lista, categoria, maximo, disponibilidad)
# f.mostrar_productos(filtrar)

