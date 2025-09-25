import os
import random
import time
import platform

randomPosX=random.randint(0,50)
randomPosY=random.randint(0,50)
barcoEnemigo=[randomPosX, randomPosY]
cont=0
barcoDestruido=False


def limpiarPantalla():
    if platform.system() == "Windows":
        os.system("cls");
    else:
        os.system("clear");

posicionBarcoX=int(input("==================================================\nComandante, ingrese la posición X del barco de guerra Ballena III\n==================================================\n"))
limpiarPantalla()
posicionBarcoY=int(input("==================================================\nComandante, ingrese la posición Y del barco de guerra Ballena III\n==================================================\n"))
limpiarPantalla()

if posicionBarcoX<=50 and posicionBarcoX>=0 and posicionBarcoY<=50 and posicionBarcoY>=0:
    comandante2=[posicionBarcoX, posicionBarcoY]
else:
    print("==================================================\n¡Comandante, las posiciones están fuera del area de combate!\n==================================================\n")
    time.sleep(2.0)
    limpiarPantalla()

PrimerDisparo=int(input("==================================================\n¡¡¡Señor!!! ¿¿Posición para disparar señor??\n==================================================\n"))
limpiarPantalla()
print("====================================================================\nEspías informan que el barco enemigo se encuentra entre los rangos marítimos: POS X/Y [50:50]\n====================================================================")
time.sleep(3.0)
limpiarPantalla()
SegundoDisparo=int(input("==================================================\n¡¡¡Señor!!! ¿¿Posición para el segundo disparo señor??\n==================================================\n"))
limpiarPantalla()

if PrimerDisparo>=0 and PrimerDisparo<=50 and SegundoDisparo>=0 and SegundoDisparo<=50:
    if barcoEnemigo[0]==PrimerDisparo and barcoEnemigo[1]==PrimerDisparo or barcoEnemigo[0]==SegundoDisparo and barcoEnemigo[1]==SegundoDisparo or barcoEnemigo[0]==SegundoDisparo and barcoEnemigo[1]==PrimerDisparo or barcoEnemigo[0]==PrimerDisparo and barcoEnemigo[1]==SegundoDisparo:
        print("====================================================================\n¡¡Inteligencia aerea informa que hemos hundido el barco enemigo!!!\n====================================================================")
        limpiarPantalla()
        barcoDestruido=True
    else:
        print("====================================================================\n¡¡Hemos vuelto a darle al agua SEÑOR!! Inteligencia informa que la posición del enemigo es:", barcoEnemigo[0:2],"\n====================================================================")
        limpiarPantalla()
else:
    print("====================================================================\n¡¡Hemos vuelto a darle al agua SEÑOR!! Inteligencia informa que la posición del enemigo es:", barcoEnemigo[0:2],"\n====================================================================")
    limpiarPantalla()

if barcoDestruido==False:
    disparoEnemigo=random.randint(0,50)
    segundoDisparoEnemigo=random.randint(0,50)
    if disparoEnemigo==posicionBarcoX and disparoEnemigo==posicionBarcoY or segundoDisparoEnemigo==posicionBarcoX and segundoDisparoEnemigo==posicionBarcoY or disparoEnemigo==posicionBarcoX and segundoDisparoEnemigo==posicionBarcoY or segundoDisparoEnemigo==posicionBarcoX and disparoEnemigo==posicionBarcoY:
        print("====================================================================\n¡¡ALERTA!! ¡¡El barco enemigo nos ha dado!!\n====================================================================")
        limpiarPantalla()
    else:
        print("====================================================================\nPor suerte nuestro enemigo ha fallado los disparos\n====================================================================")
        limpiarPantalla()

print("LA GUERRA HA TERMINADO, VOLVAMOS A CASA...")
time.sleep(3.0)
limpiarPantalla()

