def buscar_por_id(servidores, identificador)
    for x in servidores:
        if identificador == x["id"]:
            return x
    return None

id = int(input("identificador:"))
res = buscar_por_id(SERVIDORES, id)

ir res == None:
    print("No encontrado")
else
    print("Encontrado")
    mostrar_inventario([res])


if __name__ == '__main__':
    print(" ¡¡¡ Solo se imprime si se invoca al modulo")
    print(__name__)