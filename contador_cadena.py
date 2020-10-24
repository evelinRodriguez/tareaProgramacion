
def LenN (cadena):
    cont=0
    for caract in cadena:
        cont+=1
    return cont

producto= "coco"
cuantos= LenN(producto)
print(cuantos)