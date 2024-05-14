import os
import time
principal=True
tele=True
menu=True
cilin=True

finalc=0
totalfinal5=0
totalfinal15=0
totalfinal45=0
totalfinalkilos=0

finalc=0
camionstan=0

while principal==True:
    secundario=True
    while secundario==True:
        os.system("cls")
        nombre=(input("Ingrese nombre de cliente\t:"))
        rnombre=len(nombre)
        if rnombre<3:
            print("El nombre debe tener mas de 3 letras")
            time.sleep(2)
        elif rnombre>3:
            while tele==True:
                try:
                    telefono=(input("Favor ingrese numero de cliente\t:"))
                    rtelefono=len(telefono)
                except ValueError:
                    print("debe ser un valor numerico")
                    continue
                if rtelefono<8 or rtelefono>9:
                    print("El numero de de ser mayor que 8 y menor que 9")
                    continue                  
                else:
                    tele=False
                    secundario=False 
    while menu==True:
        os.system("cls")
        try:
            opcion=int(input("1. Compra camion estandar\n2.Compra entrega carga especifica\n3.Imprimir boleta y cerrar pedido\nElija opcion\t:" ))
        except ValueError:
            print("Debe ser un valor numerico")
            time.sleep(2)
            continue
        if opcion<1 or opcion>3:
            print("Error de eleccion, debe ser entre 1 y 3")
            menu=True
        
        elif opcion==1:
            cantidadcamionestan=int(input("Ingrese cantidad de camiones a contratar\t:"))
            camionstan=camionstan+cantidadcamionestan
            totalcamion=cantidadcamionestan*450
            finalc=finalc+totalcamion            
        
        elif opcion==2:
            while cilin==True:
                try:
                    os.system("cls")
                    cilindros=int(input("CANTIDAD DE CILINDROS A COMPRAR\n1.cilindro de 5kilos\n2.cilindro de 15 kilos\n3.cilindro de 45 kilos\n\nElija opcion\t:"))
                except ValueError:
                    print ("Debe ser un valor numerico")
                    time.sleep(2)
                    continue
                if cilindros<1 or cilindros>3:
                    print("El valor ingresado no esta en el menu") 
                    time.sleep(2)
                    continue
                
                elif cilindros==1:
                    cil5=int(input("ingrese cantidad de cilindros de 5kilos a comprar"))
                    total5=cil5*5
                    totalfinal5=totalfinal5+total5

                elif cilindros==2:    
                    cil15=int(input("ingrese cantidad de cilindros de 15 kilos a comprar"))
                    total15=cil5*15
                    totalfinal15=totalfinal15+total15
                
                elif cilindros==3:
                    cil45=int(input("ingrese cantidad de cilindros de 45 kilos a comprar"))
                    total45=cil5*45
                    totalfinal45=totalfinal45+total45
                seguirc=(input("¿DESEA SEGUIR COMPRANDO 1.SI  2.NO ? "))
                if seguirc==1:
                    cilin=True
                elif seguirc==2:
                    totalfinalkilos=totalfinal5+totalfinal15+totalfinal45
                    divkilos=totalfinalkilos/450
                    residuokilos=totalfinalkilos % 450
                    cilin=False
                    menu=True
        elif opcion==3:
            ##menu=False
            #os.system ("cls")
            cancamiones=finalc+totalfinalkilos
            cancamiones1=cancamiones/450
            print ("─"*30)
            print ("\nDETALLE")
            print ("─"*30)
            print (f"Nombre de Cliente\t\t: {nombre}")
            print (f"Telefono de cliente\t\t: {telefono}")
            print ("─"*30)
            print (f"Cantidad de Kilos\t: {finalc+totalfinal5+totalfinal15+totalfinal45}")
            print (f"Cantidad de camiones\t: {cancamiones1}")
            print ("TOTAL\t\t: {}")
    











