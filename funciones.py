def mensaje ():
    print(("hola"))

#llamar la funcion
mensaje()


#funcion con parametro

def mensaje2 (nombre): #nombre=cad
    print("hola" , nombre)


  #para llamarla
cad= input("ingrese nombre")# se crea la variable
mensaje2(cad)# le ingresamos el paramentro

#funcion retorno

def mensaje3(nombre):#nombre = nom
    cadena= "hola"+nombre
    return cadena
nom=input("ingresar nombre")
cadenaRetorno=mensaje3(nom)#cadenaRetorno= cadena
print(cadenaRetorno)


#para saber cuantos caracteres tiene una cadena

def LenN (cadena):
    cont=0
    for caract in cadena:
        cont+=1
    return cont

producto= "coco"
cuantos= LenN(producto)
print(cuantos)

#para validad una entrada de dato

def validar_num (cadena):
    while not cadena.isdigit():
        cadena=input("error ,  ingrese otro")
    return int(cadena)

cadena= input("ingrese numero")
numero= validar_num(cadena)
print(numero)

