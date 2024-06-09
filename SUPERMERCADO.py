import os
import time
import csv
productos={} #creacion de diccionario vacio
canasta={}   #creacion de diccionario vacio   

principal=True 
while principal==True:  #mientras la variable "principal" sea = a True, hacer.
    os.system("cls")    #borrado de pantalla,impresion de menu y obtencion de valor "menu", con control de errores try
    try :
        menu=int(input("Opciones de bodega \n[1]...Ingrese productos a Bodega\n[2]...Guarde productos y valor a archivo scv\n\nOpciones de Compras\n[3]...Agrege productos a la canasta\n[4]...Ver canasta\n[5]...Salir\nElija Opcion : "))
    except ValueError:
        print("Opcion incorrecta, dede ser un valor numerico")
        time.sleep(2)
        continue
    
    if menu==1:   #si el valor de de la variable "menu" = 1, entonces.
        a=True
        while a==True:
            producto=input("Ingrese nombre del producto : ")
            try:
                precio=int(input("Ingrese el precio a publico :"))
            except ValueError:
                print("Error, debe ser un valor numerico")
                time.sleep(2)
                continue
            productos[producto]=precio      #llenando el diccionario {productos} con el valor de la variable "producto" y "precio" ingresada por usuario 
            print(productos)                #Imprimiendo por pantalla el contenido del diccionario {productos}
            otro=input("Desea agregar otro producto S/N :")
            if otro=="S" or otro=="s":
                continue
            elif otro=="N" or otro=="n":
                os.system("cls")
                break
            else:
                print("Opcion no valida")
                time.sleep(2)
                os.system("cls")
                continue
    
    elif  menu==2:                                                                # Si el valor de la variable "menu" = 2, entonces:
        with open ("productosyprecios.csv","w",newline="") as productosyprecios:  # Creamos un nuevo archivo con permiso de escritura y le damos un alias
            escritor_csv=csv.writer(productosyprecios)                            # Creamos un objeto escritor de CSV asociado al archivo.
            for k,v in productos.items():      # Recorremos sobre cada clave y valor en el diccionario {productos}. "k"=primer valor de keys() y "v"=primer valor de values() 
                escritor_csv.writerow([k,v])                                      # Escribimos una fila en el archivo CSV con la clave y el valor. 
                      
    elif menu==3:      #si el valor de la variable "menu" = 3, entonces:
        b=True
        while b==True:
            print ("─"*150)
            print ("P R O D U C T O S   :    P R E C I O  ")
            print ("─"*150)  
            print (productos)
            print ("─"*150)
            selec=input("Ingrese producto para agregar a la canasta : ") 
            if productos.get (selec):    #si en el diccionario {productos}, se encuentra el valor de la variable "selec" ingresada por usuario, entonces: 
                pre=productos[selec]     #se asigna el precio del producto a la variable "pre"
                                
                canasta[selec]=pre       #llenado del diccionario {canasta} con el valor de la variable "selec" y "pre" 
                print(canasta)           #se imprime por pantalla el diccionario {canasta}   
                ot=input("Agrega otro producto S/N :")
                if ot=="S" or ot=="s":
                    continue
                elif ot=="N" or ot=="n":
                    break
            else:
                print("Producto no existe en bodega")
                time.sleep(2)
                t=input("Agrega otro producto S/N :")
                if t=="s" or t=="S":
                   os.system("cls")
                   continue
                else:
                    break

    elif menu==4:                  
        os.system("cls")
        print("─"*100)
        print("C A N A S T A ")
        print("─"*100)
        for elemento in canasta:     # Iniciando ciclo (for) ## la variable "elemento" empezara en 0 y llegara hasta la cantidad de valores ingresadas en el diccionario {canasta}
            val=canasta[elemento]    # se obtiene el valor del elemento en la canasta y se le asigna a la variable "val"
            print (f"{elemento} {val}")
            
        suma=sum(canasta.values())  # Se realiza suma de todos los valores correspondiente a los values() del diccionario {canasta} 
        print("─"*100) 
        print (f"TOTAL : {suma}")
        print("─"*100)
        i=input("presione [Enter] para continuar ")
        principal=True
        continue        

    elif menu==5:                #si el valor de de la variable "menu" = 5, entonces:
        principal=False          #Se asigna valor False a variable "principal" , sale de ciclo.



