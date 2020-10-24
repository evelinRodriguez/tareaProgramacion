'''
if
ejemplos : calcular el promedio de un alumno
'''
nombre = input("ingrese nombre")

matematicas = float(input(nombre + " ingresar calificacion matematicas "))
quimica = float(input(nombre + " ingresar calificacion quimica "))
español = float(input(nombre + " ingresar calificacion español "))

promedio = ( matematicas + quimica + español) /3
#ingresar if

if promedio <=2.9:
     print('perdio' , nombre  )

