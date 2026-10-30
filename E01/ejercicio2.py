frase = "Python es divertido"
frase_invertida = frase[::-1]
print ("frase.lower:", frase.lower())
print ("logitud frase:", len(frase))

busca = "PYTHON"

if busca.lower() in frase.lower():
    print ("SI esta")
else:
    print ("No esta")

print ("frase al reves:", frase_invertida)
