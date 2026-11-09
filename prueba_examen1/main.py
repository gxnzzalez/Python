from servidores import SERVIDORES # , LISTAUNO, lo que hago es importar algo concreto de un modulo
import funciones as f  #importo el modulo completo y le pongo el nombre f, que se utiliza al hacer una funcion al ponerlo delante de la funcion

servidores_encendidos = f.filtras_por_estado(SERVIDORES, "encendido")
f.mostrar_inventario(servidores_encendidos)

servidores_apagados = f.filtras_por_estado(SERVIDORES, "apagado")
f.mostrar_inventario(servidores_apagados)

