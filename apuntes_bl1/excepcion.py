import os

ruta = input("Directorio a crear: ")

try:
    os.mkdir(ruta)

except FileExistsError:
    print("El directorio ya existe")

except PermissionError:
    print("No tiene permisos para crear el directorio")

except FileNotFoundError:
    print("Algún directorio intermedio no existe")

except Exception as e:
    print("Se ha producido un error no previsto:")
    print(e)

else:
    print("Directorio creado correctamente")

finally:
    print("Fin del intento de creación")