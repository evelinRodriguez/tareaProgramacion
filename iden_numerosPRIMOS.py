'''
IDENTRIFICAR SIU UN NUMERO ES PRIMO
'''

num= int(input("ingrese numero :"))
cont=0

if num>1:
    for i in range(2,num):
        resto= num%i
        if resto==0:
            cont+=1
    if cont==0:
        print(" el numero es primo")
    else:
        print("no primo")
else:
    print("no es primo ")


