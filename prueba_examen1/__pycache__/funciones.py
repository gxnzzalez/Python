# from servidores import SERVIDORES, LISTAUNO

def mostrar_resumen(servidores):
    res = calcular_resumen(servidores)

    print("Total:", res["total"])
    print("Encendidos:", res["encendido"])
    print("Apagados:", res["apagado"])
    print("Disponibilidad:", res["disponibilidad"])



def calcular_resumen(servidores):
    """Calcula indicadores solo con lecturas de equipos encendidos"""
    resultado = {
        "total": 0,
        "encendidos": 0,
        "apagados": 0,
        "disponibilidad": 0
    }
    resultado["total"] = len(servidores)
    le = filtras_por_estado(servidores, "encendido")
    resultado["encendido"] = len(le)
    resultado["apagado"] = resultado["total"] - resultado["encendido"]
    resultado["disponibilidad"] = 100 * (resultado["encendido"]/resultado["total"])

    return resultado

# def mostrar_inventario(lista):

# def filtras_por_estado(servidores, estado):
#     """Devuelve una lista con el estado de los servidores"""


# #Return lista, recorremos cumpliendo una condicion, puedo poner sevidor/es o la x
# return [ servidor for servidor in servidores if x["estado"] == estado ]

# lista = [ x for x in servidores if x["estado"] == estado ]
# return lista

def buscar_por_id(servidores, identificador):
    for x in servidores:
        if identificador == x["id"]:
            return x
    return None

# id = int(input("identificador:"))
# res = buscar_por_id(SERVIDORES, id)

# ir res == None:
#     print("No encontrado")
# else
#     print("Encontrado")
#     mostrar_inventario([res])


# if __name__ == '__main__':
#     print(" ¡¡¡ Solo se imprime si se invoca al modulo")
#     print(__name__)