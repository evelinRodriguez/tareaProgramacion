#sentencias anidadas

print("conversor")
opcion = int(input("presiona 1  para convertir numero a palabra \n presiona 2 para convertir de palabra a numero"  ))

if opcion==1:
    num= int(input("ingrese numero que quiere convertir"))

    if num == 1:
        print("es el numero  uno ")
    elif num == 2:
        print("el numero es dos")
    elif num == 3:
        print("es el tres")
    elif num == 4:
        print("es el cuatro")
    elif num == 5:
        print("es el 5")
    else:
        print("solo conbvertimos de 1 a 5 sorry")
elif opcion ==2:
    palabra = str(input("ingrese palabra"))

    if palabra == 'uno' :
        print("es el numero  1 ")
    elif palabra == 'dos':
        print("el numero es 2")
    elif palabra == 'tres':
        print("es el 3")
    elif palabra == 'cuatro':
        print("es el 4")
    elif palabra == 'cinco':
        print("es el 5")
    else:
        print("solo convertimos de uno a cinco sorry")
else:
    print("solo hay 2 opciones")