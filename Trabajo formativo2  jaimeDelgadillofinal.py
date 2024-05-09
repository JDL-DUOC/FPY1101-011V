import os
import time
os.system ("cls")
i=True
totalpik=0
totalota=0
totalpul=0
totalang=0
cupondes="soyotaku"
descuento=0
principal=True
while principal==True:
    while i==True:
        opc=int(input("MENU\n1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800\n\nIngrese su pedido : "))
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
            descuento=(totalfinalsincupon*10)/100

        
        elif ingresecupon != cupondes:
            print("su cupon no es valido")
            time.sleep(2)
            totalpedido=totalfinalsincupon
        
    elif cupon==2:
        totalpedido=totalfinalsincupon
        i=False        
    os.system("cls")
    print ("─"*30)
    print ("cantidad de productos ", )
    print ("─"*30)
    print (f"Pikachu Roll\t\t:{totalpik/4500:.0f}")
    print (f"Otaku Roll\t\t:{totalota/5000:.0f}")
    print (f"Pulpo Venenoso\t\t:{totalpul/5200:.0f}")
    print (f"Anguila Electrica\t:{totalang/4800:.0f}")
    print ("─"*30)
    print (f"subtotal\t\t:{totalfinalsincupon:.0f} ")
    print (f"Descuento\t\t:{descuento:.0f} ")
    print (f"TOTAL\t\t\t:{totalfinalsincupon-descuento:.0f}")
    print("─"*30)
    otro=int(input("Desea otro pedido 1.si 2.no   : "))
    if otro==1:
        os.system("cls")
        totalpik=0
        totalota=0
        totalpul=0
        totalang=0
        cupondes="soyotaku"
        descuento=0
        i=True
    elif otro==2:
        principal=False
print("Adios")        
      

            



