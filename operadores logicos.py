#operadores logicos


print("conjuncion (and)")
num1=int(input("escriba un numero mayor que 2 y menor a 5"))

if num1 > 2 and num1 < 5 :
    print("el numero " , num1 , " cumploe condicion ")
else:
    print("no se cumple")

print("disyuncion (or)")

palabra= input("para cumplir escriba si o yes")

if palabra == "si" or palabra== "yes":
    print("cumple")
else:
    print("no cumple")

print("negacion (not)")
num2= int(input(" introduce numero =  a 5"))
if not num2==5:
    print("cumple")
else:
    print("no cumple")