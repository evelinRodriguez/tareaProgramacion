'''
preguntar cuantos numeros desea ingresar
mostrar cuantos son pares
mostrar suma de impares
'''
veces= int(input("cuantos numeros desea ingresar = "))
cont=0#va afuera para que no se resetee , si se pone dentro del cilo se vuelve apponer en 0
acum=0
for i in range(veces):

    num= int(input("ingrese numero : "))
    if num%2==0: #para contar cuantos pares inicializar el contador
       cont+=1 #contador va sumando de a 1 cont=cont +1
    else:
        acum+=num

print( " total de pares es :" , cont)
print("suma impares es : ",acum)