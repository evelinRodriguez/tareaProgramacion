'''
Ejercicio1
usuario ingresa numero
determina años, meses y semanas vividas


def vida (numero):
    años= numero//360
    meses= años*12
    semanas= (años*360)//7
    return años , meses,semanas
num=int(input("ingrese dias vividos completamente"))
Variables=vida(num)

#print("años , meses , semanas :" ,Variables )# para imprimir resultado de ejercicio1
'''

'''
Ejercicio2
usuario ingresa numero
identificar si numero es primo primos

def fprimo(numero):
    cont=0
    if numero > 1:
        for i in range(2, numero):
            resto = numero % i
            if resto == 0:
                cont += 1
        if cont == 0:
            print(" el numero es primo")
        else:
             print("no primo")



num= int(input("ingrese numero"))
fprimo(num)
'''

'''
Ejercicio3
usuario ingresa numero
detrminar cuantos digitos tiene


def fdigitos(numero):
    digitos=0
    for i in numero:
        i.isdigit()
        digitos+=1
    return digitos


num= input("igrese numero")
resultado= fdigitos(num)
print( " cantidad de digitos" + str(resultado))

'''

'''
Ejercicio 4
igresar numero
retornar sumatoria de los primos

def sumaPrimo (numero):

    acum=0
    for i in range(2, numero):
            resto = numero % i
            if resto == 0:
                acum+=i

    return acum

num= int(input("ingrese numero"))
resultado=sumaPrimo(num)
print("suma de los primos" + str(resultado))
'''

'''
Ejercicio 5
ingresar numero
determinar factorial del mismo 


def factorial(numero):
    resultado=numero

    for i in range(numero-1 , 1 , -1):
        resultado=resultado*i
    return resultado

num= int(input("ingrese numero :"))
fact=factorial(num)
print("el fatorial del numero es :" + str(fact))
'''