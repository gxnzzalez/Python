# Ejemplo uso format en print
nombre = "Alfredo Zumberg"
edad = 23
altura = 1.915
print(nombre, "su edad es", edad, "y altura", altura)
# con format
print(f"{nombre} su edad es {edad} y altura {altura:.1f}")  #f nos indica que la cadena tiene formato, si no tiene f y tiene llaves no funciona. El .1f nos indica que cogamos un decimal, es decir el numero despues del . indica los deciamles
# print("{nombre} su edad es {edad} y altura {altura:.1f}")

## Algunos métodos de string

saludo = "Hola Mundo"
print("saludo:", saludo)

print("saludo,lower():", saludo.lower())
print("saludo:", saludo)
# # No modifica cadena original. 
# # Si queremos modificar hace falta asignación

saludo = saludo.lower()
print("saludo:", saludo)

# # Replace, lo mismo..
print("saludo.replace():", saludo.replace("mundo", "universo"))
print("saludo:", saludo)

# # str como array o lista, longitud o tamaño del str
saludo ="¡Hola mundo!"
print("Primer carácter:", saludo[0])  #se indexa desde 0
print("Segundo carácter:",saludo[1])
print("Longitud saludo:", len(saludo)) #len es la longitud. Si la longitud es 12 en realidad es 11 porque se empieza por el 11

# # Buscar en un str: in y not in

texto = "The best thiNgs  life are free!"
busca = "FREE"

#Quiero que lo encuentre da igual mayuscula o minuscula
if busca.lower() in texto.lower():
    print("¡¡Sí está!!")
else:
    print("No está")

#Solo lo encuentra si son iguales
if busca in texto:
    print("¡¡Sí está!!")
else:
    print("No está")

# # o en negativo
if busca not in texto:
    print("No está")
else:
    print("¡¡Sí está!!") 
# # Proponer: no case sensitive


# # Concatenar str

nombre = "Raquel"
apellidos = "García Ross"
print(nombre + " " + apellidos) 

nombreCompleto = apellidos + ", " + nombre
print(nombreCompleto)

# # Recorrer str
for x in nombre:
    print(x)

# # con índices
for i in range(len(nombre)):
    print(f"{i}: {nombre[i]}")