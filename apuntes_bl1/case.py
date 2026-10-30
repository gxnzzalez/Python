opcion = int(input("Seleccione una opción")) 

match opcion:
    case 0:
        print("Ha seleccionado opción 0")
        print("procedemos")
    case 1:
        print("Ha seleccionado opción 1")
        print("procedemos")

    # ...

    case _:   #este es el caso por defecto
        print("por defecto")
        print("cuando no se le ha indicado ninguna de las opciones contempladas")
        