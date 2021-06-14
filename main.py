""" Programa rostros#
    Programa para el manejo de rostros codificados 
    incorpora al modulo rostros.py
    Oscar Franco-Bedoya
    Junio 2-2021 """

#---------------- Zona librerias------------
import rostros as rt

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

id = input("ingrese el id del rostro:")

f = open("rostros.txt", "r")
rostros = f.read()
#print(rostros[2])


if rostros.find(id) != -1:
  rostros = rostros.split("---")
  rostro1 = rostros[0].split(id)
  codigos_rostro=rt.cargar_rostro(rostro1[1])
  #print(rostro1[1])
  rt.imprimir_rostro(codigos_rostro)
else:
  print("no existe")

