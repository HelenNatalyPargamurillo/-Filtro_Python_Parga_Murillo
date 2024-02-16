import json
import os 
import Funciones.TITULO
import Funciones.administracion

"""bienvenido a Mi Movistar"""



adm=True

while adm:True

menu=int(input("ingrese una opcion: \n 1.gestion de usuasrio \n 2. Fidelizacion \n servicios.  \n 4."))
print(menu)

if menu==1:
        print (Funciones.administracion.user)

if menu==2:
        print (Funciones.TITULO.servicio())
        pass

    
if menu==3:
        print (Funciones.TITULO.administracion())
        pass
    
else: 
        print (Funciones.TITULO.salir())
        pass  

