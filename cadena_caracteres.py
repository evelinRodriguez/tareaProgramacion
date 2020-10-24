#operador+-

mensaje ="hola"
mensaje += " "
mensaje += "ernesto"
print (mensaje)

 #concatenacion

print("concatenacion:")
mensaje1 = "hola"           #asignacion de caracteres
espacio = " "
nombre = "ernesto"

#concatenacion numerico

print("concatenacion ejemplo 1:")
print(mensaje1 + espacio + nombre)

numero1 = 4
numero2 = 6
resultado = numero1 + numero2
#importante convertir valos numero a string o no compila
resultado = str(resultado)

print("resultado de una suma es :" + resultado)

#busqueda
print("busqueda")
mensaje2 = "hola ernesto"
buscar_subcadena = mensaje2.find("ernesto")
print(buscar_subcadena)
#al imprimir indica en que posicion esta

#extraccion cadena
print("cadena")
mensaje3 = "hola ernesto"
extraer_Cadena = mensaje3[1:8 ]
print (extraer_Cadena)

#comparacion
print("comparacion")
mensaje4 = "hola"
mensaje5 = "hola"
mensaje4 == mensaje5

print(mensaje4 == mensaje5)