#operadores relacionales
print("comparacion de dos numeros")
num1= int(input("ingrese numero 1 :"))
num2=int(input("ingrese numero 2 :"))
print("numeros a comparar " , str(num1) + "y" , str(num2))

if num1<num2:
    print("el" , str(num1) , "es menos que" , str(num2))
if num1>num2:
    print("el", str(num1), "es mayor que", str(num2))
if num1==num2:
    print("el", str(num1), "es igual que", str(num2))
if num1!=num2:
    print("el", str(num1), "es diferente a ", str(num2))
if num1<=num2:
    print("el", str(num1), "es menor o igual", str(num2))
if num1>=num2:
    print("el", str(num1), "mayor o igual", str(num2))
else:
    print("nose")