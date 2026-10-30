# lógica o booleana
autorizado = False    # el otro valor posible True
print( type(autorizado)  )

if autorizado==True:  # autorizado==True <=> autorizado 
    print("Puede pasar")
    print("segundo")
else:
    print("No puede pasar")

#ejemplo
edad = input ("Edad: ")

print(edad, type(edad))
edad = float(edad)
print(edad, type(edad))

if edad<21:
    print("edad menor 21")
else:
    print("edad mayor o igual de 21")
print("tras if")

#adaptacion
if 21<edad and edad<25:
    print("entre 21 y 25")
else:
    print("no entre 21 y 25")
print("tras if")

print (edad +1)
print (edad *2)
print (edad /4)

# saldo = 100000
# edad = 16
# if (edad > 18 or saldo > 50000):
#     print("Puede apostar")
# else:
#     print("No puede apostar")