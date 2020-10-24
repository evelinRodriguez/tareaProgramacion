'''
tres departamentos:
1.altencion al cliente clave1
1 año servicio --> 6 dias vacaciones
2 a 6 años servisio -->14 dias vacaciones
7 o mas años de servicio -->20 dias de vacaciones
2.logistica clave 2
1 año servicio --> 7 dias vacaciones
2 a 6 años servisio -->15 dias vacaciones
7 o mas años de servicio -->22 dias de vacaciones
3. gerencia clave 3
1 año servicio --> 10 dias vacaciones
2 a 6 años servisio -->20 dias vacaciones
7 o mas años de servicio -->30 dias de vacaciones

'''

print("dias de vacaciones")
nombre= input("ingrese su nombre : ")
clave = int(input("ingrese clave de su departamento"))
años= int(input("años laborados"))

#print( "su nombre es :  " , nombre + " \n  su clave es  ", str(clave) )

if clave==1:
    if años ==1:
        print("nombre :", nombre , "\n clave : ", str(clave) , "\n dias de vacaciones es 6" )
    elif años>1 and años<=6:
        print("nombre :", nombre, "\n clave : ", str(clave), "\n dias de vacaciones es 14")
    elif años>7:
        print("nombre :", nombre, "\n clave : ", str(clave), "\n dias de vacaciones es 20")
elif clave==2:
    if años ==1:
        print("nombre :", nombre , "\n clave : ", str(clave) , "\n dias de vacaciones es 7" )
    elif años>1 and años<=6:
        print("nombre :", nombre, "\n clave : ", str(clave), "\n dias de vacaciones es 15")
    elif años>7:
        print("nombre :", nombre, "\n clave : ", str(clave), "\n dias de vacaciones es 22")
elif clave==3:
    if años ==1:
        print("nombre :", nombre , "\n clave : ", str(clave) , "\n dias de vacaciones es 10" )
    elif años>1 and años<=6:
        print("nombre :", nombre, "\n clave : ", str(clave), "\n dias de vacaciones es 20")
    elif años>7:
        print("nombre :", nombre, "\n clave : ", str(clave), "\n dias de vacaciones es 30")
else:
    print("departamento no existe")