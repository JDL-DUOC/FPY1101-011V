import os
import time
os.system ("cls")
i=True
totalpik=0
totalota=0
totalpul=0
totalang=0
cupondes="soyotaku"
while i==True:
    opc=int(input("MENU\n1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800\nIngrese su pedido : "))
    cantidad=int(input ("Elija cantidad : "))
    if opc<1 or opc>4:
        print ("Eleccion no valida")
        time.sleep(2)
        i=True
    elif opc==1:
        cantpik=cantidad*4500
        totalpik=totalpik+cantpik
    elif opc==2:
        cantota=cantidad*5000
        totalota=totalota+cantota
    elif opc==3:
        cantpul=cantidad*5200
        totalpul=totalpul+cantpul
    elif opc==4:
        cantang=cantidad*4800
        totalang=totalang+cantang
    
    otropedido=int(input("Desea agregar mas productos a su pedido 1.si 2.no "))
    if otropedido==1:
        os.system ("cls")
        i==True
    elif otropedido==2:
        i=False
os.system ("cls")
totalfinalsincupon=totalpik+totalota+totalpul+totalang
print ("El total de su pedido es: " , totalfinalsincupon)
cupon=int(input("Usted tiene un cupon de descuento 1.si 2.no  : "))
if cupon==1:
    ingresecupon=(input("Favor ingrese el codigo de descuento : "))
    if ingresecupon==cupondes:
        totalpedido=(totalfinalsincupon)/1.10 
    elif ingresecupon != cupondes:
        print("su cupon no es valido")
        time.sleep(2)
        totalpedido=totalfinalsincupon
elif cupon==2:
    totalpedido=totalfinalsincupon
    i=False        
os.system("cls")
print ("*"*30)
print ("cantidad de productos ", )
print ("*"*30)
print ("Pikachu Roll\t:")
print ("Pulpo Venenoso\t:")

##Pikachu Roll : 2 Otaku Roll :1
##Pulpo Venenoso Roll:1 Anguila Eléctrica Roll:0
##****************************** Subtotal por pagar: $19200
##Descuento por código: $1920 TOTAL: $17280

         
            



