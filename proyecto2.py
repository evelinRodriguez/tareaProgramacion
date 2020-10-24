'''
pedir numero
indicar si el numero es par o impar
'''

numero = int(input("ingrese numero : "))

i= numero % 2

if i==0:
    print("el numero " , str(numero) , "es par")
else:
    print("el numero ", str(numero), "es impar")

