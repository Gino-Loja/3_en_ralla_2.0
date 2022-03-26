from   colorama  import  init,Fore
init(autoreset = True )
import os
import time
import random
ma = [""]*9
x = 0

listax = []
def tablero (table,listaGanadora,fichas):
    k=0
    for i in range(3):
        print("\t"," ------------------------- ")
        for j in range(3):
            for m in listaGanadora:

                if m == k and fichas== yo :
                    ma[k] = Fore.RED + ma[m]

                elif m == k and fichas == maquina :
                     ma[k] = Fore.BLUE + ma[m]

            print("\t"," | ",ma[k], end=" ")
            k=k+1
        print("\t"," | ")
    print("\t"," ------------------------- ")


def jugadayo(table,posicion):
    global x

    if turno[x%2]==yo:
        if table[posicion-1] != "":
            print()
            print("La casilla esta ocupada ")
            print()
            x = x-1
        else:

            table[posicion-1] = yo
            lista.append(posicion)


def jugadaEl(table,posicion):
    global x


    if table[posicion-1] != "":
        print()
        print("La casilla esta ocupadas")
        print()
        x = x-1
    else:

        table[posicion-1] = maquina
        lista.append(posicion)



def jugadaMaquina(table,posiciom):
    n=0

    while True :

           i=0

           while i < len(lista):

               if lista[i] != posiciom:
                   n=n+1

               i=i+1

           if n == len(lista):

               if turno[x%2]==yo:

                   lista.append(posiciom)
                   table[posiciom-1] = yo
                   break

               lista.append(posiciom)
               table[posiciom-1] = maquina
               break


           elif len(lista)==9:
                break
           else:
               posiciom = random.randint(1, 9)

           n=0

           i= 0

def Ganador(table):
    l = 0
    n=0
    ganador = True
    f = ""
    d= [11]
    for i in range(3):
        if table[i] == yo:
            n = n+1
            if n==3:
                ls=[0,1,2]
                ganador = False
                return ganador,yo,ls

        if table[i] == maquina:
            l = l+1
            if l==3:
                ls=[0,1,2]
                ganador = False
                return ganador,maquina,ls
    l=0
    n=0
    for i in range(3,6):
        if table[i] == yo:
            n = n+1
            if n==3:
                ls=[3,4,5]
                ganador = False
                return ganador,yo,ls

        if table[i] == maquina:
            l = l+1
            if l==3:
                ls=[3,4,5]
                ganador = False
                return ganador,maquina,ls
    l=0
    n=0
    for i in range(6,9):
        if table[i] == yo:
            n = n+1
            if n==3:
                ls=[6,7,8]
                ganador = False
                return ganador,yo,ls

        if table[i] == maquina:
            l = l+1
            if l==3:
                ls=[6,7,8]
                ganador = False
                return ganador,maquina,ls
    l=0
    n=0
    if table[0]== table[4]== table[8] != "" :
        ganador = False
        ls=[0,4,8]
        return ganador,table[8],ls


    elif table[2]== table[4]== table[6] != "":
        ganador = False
        ls=[2,4,6]
        return ganador,table[6],ls

    elif table[0]==table[3]== table[6] != "":
        ganador = False
        ls=[0,3,6]
        return ganador,table[6],ls

    elif table[1]==table[4]== table[7] != "":
        ganador = False
        ls=[1,4,7]
        return ganador,table[7],ls

    elif table[2]== table[5]==table[8] != "":
        ls=[2,5,8]
        ganador = False
        return ganador,table[8],ls
    i=0
    n=0
    for i in table:
        if i == "":
            n = n+1
    if n==0 :
        f = "empate"
        ganador = False
        return ganador,f,d

    return ganador,f,d



def jugamaMaestra():
    mejor = -float("inf")

    for i in range(9):
        if ma[i]=="":

            ma[i] = maquina
            punto = minimax(ma,0,False)
            ma[i] = ""

            if punto > mejor:
                mejor = punto
                mover = i


    ma[mover] = maquina


def minimax(ma,depth, isMaximizing):
    result,fic,a = Ganador(ma)
    if fic != "":
        return puntos[fic]

    if isMaximizing:
        mejor = -float("inf")
        for i in range(9):
            if ma[i]=="":
                ma[i] = maquina
                punto = minimax(ma,depth+1,False)
                ma[i] = ""
                if  iaMaquina == 2:
                    mejor = punto
                else:
                    mejor = max(punto, mejor)

        return mejor
    else:
        mejor = +float("inf")
        for i in range(9):
            if ma[i]=="":
                ma[i] = yo
                punto = minimax(ma,depth+1,True)
                ma[i] = ""
                if  iaMaquina == 2:
                    mejor = punto
                else:
                    mejor = min(punto, mejor)

        return mejor

def posicionesDelTablero():
    print()
    print("posiciones del tablero: ")
    y=0
    for i in range(3):
        print("\t"," ------------------------- ")
        for j in range(3):
            matrix.append(y+1)
            print("\t"," | ",matrix[y], end=" ")
            y=y+1
        print("\t"," | ")
    print("\t"," ------------------------- ")
    print()

def salirJuego():
    os.system("cls")
    ru=1
    for h in range(5):
    	for c in range(2):
	    		time.sleep(0.08)
	    		os.system("cls")
		    	print('|','■'*ru,'|' ,(ru*10),'% saliendo del juego',end='')
		    	print('\n')
		    	ru+=1

def imprimerGanador():
    global n,n1

    if fichas == "empate":
        print(Fore.YELLOW+"    #### EMPATE ####")


    elif fichas==yo:
        print()
        print(Fore.RED+"       #### gano "+fichas+" ####")
        n1+=1


    else:
        print()
        print(Fore.BLUE+"     #### gano "+fichas+" ####")
        n+=1



############### DESARROLLO  DEL JUEGO#####################
""""
palabra  = "TRES EN RALLA"
print()
for h in palabra:
    print("",h,end="")
    time.sleep(0.2)

"""
elige = 1
salirDelJuego = 1

while salirDelJuego != 0:
    modoJuego=0
    elige = 1
    iaMaquina=0
    n=0
    n1=0

    while modoJuego != 1 and modoJuego != 2 and modoJuego != 3:
        os.system("cls")
        print()
        print("1. maquina vs maquina")
        print("2. jugador vs maquina")
        print("3. jugador vs jugador")
        modoJuego = int(input("Elige el modo de modo Juego: "))


    if modoJuego == 1:
        yo= "X"
        maquina= "O"
        turno = (yo,maquina)

    if modoJuego == 2:

        while iaMaquina!= 1 and iaMaquina != 2 and iaMaquina != 3 :
            os.system("cls")
            print()
            print("1. Facil")
            print("2. Medio")
            print("3. Dificil")
            iaMaquina = int(input("Elige la dificultad del juego: "))
        #escoge la casilla

        os.system("cls")
        print()
        print('Escoge la letra con la quieras jugar [X],[O]')
        ficha = input()
        ficha = ficha.upper()
        while ficha != 'X' and ficha !='O':
          ficha = input('solo escoge las letras que se muestran')
          ficha = ficha.upper()

        if ficha =='X':
            yo = ficha
            maquina = 'O'
            puntos = {
                "O": 1
                ,"X": -1
                ,"empate": 0
            }
        else:
            yo = ficha
            maquina = "X"
            puntos = {
                "X": 1
                ,"O": -1
                ,"empate": 0
            }
        turno = (yo,maquina)

    #""" falta de hacer no vale hay que darle el turno a cada jugada"""
    if modoJuego == 3:
        os.system("cls")
        print()
        print('Escoge la letra con la quieras jugar [X],[O]')
        ficha = input()
        ficha = ficha.upper()
        while ficha != 'X' and ficha !='O':
          ficha = input('solo escoge las letras que se muestran')
          ficha = ficha.upper()

        if ficha =='X':
            yo = ficha
            maquina = 'O'
        else:
            yo = 'O'
            maquina = ficha
        turno = (yo,maquina)


    while elige != 0:

        x=0

        ganar=True
        lista=[]
        ma=[""]*9
        listaGanadora=[]
        fichas=""
        matrix=[]
        os.system("cls")
        posicionesDelTablero()


        while x<9 :

            if modoJuego==1:

                if turno[x%2]==yo:
                    time.sleep(0.5)

                    a = random.randint(1, 9)
                    jugadaMaquina(ma, a)

                else:
                    num = random.randint(1, 9)
                    jugadaMaquina(ma, num)

                # jugadayo(ma, a)
                os.system("cls")
                ganar,fichas,listaGanadora = Ganador(ma)
                tablero(ma,listaGanadora,fichas)
                if ganar == False:
                    imprimerGanador()
                    break



            if modoJuego==2:

                if turno[x%2 ] == yo:

                    a = int(input('escoge la posicion (1-9): '))
                    print()

                else:

                    if iaMaquina == 1:
                        num = random.randint(1, 9)
                        jugadaMaquina(ma, num)
                    elif iaMaquina == 2:
                        jugamaMaestra()
                    else:
                        jugamaMaestra()

                if (a>=1 and  a<10) :

                    os.system("cls")
                    jugadayo(ma,a)
                    ganar,fichas,listaGanadora = Ganador(ma)
                    tablero(ma,listaGanadora,fichas)
                    if ganar == False:
                        imprimerGanador()
                        print()
                        print("Partidas ganadas: ", n1)
                        print("Partidas perdidas: ", n)
                        print()
                        break
                else:
                    print()
                    print('===ingresa numeros  del 1 al 9====')
                    x=x-1

            if modoJuego == 3:

                if turno[x%2]==yo:

                    a = int(input('escoge la posicion (1-9) : '))
                    print()
                else:
                    b = int(input('escoge la posicion (1-9) jugador 2: '))
                    print()

                if (a>=1 and  a<=9) or  (b>=1 and  b<=9) :

                    os.system("cls")

                    if turno[x%2] == maquina:
                        jugadaEl(ma,b)
                    else:
                        jugadayo(ma,a)
                    ganar,fichas,listaGanadora = Ganador(ma)
                    tablero(ma,listaGanadora,fichas)
                    if ganar == False:
                        imprimerGanador()
                        print()
                        print("Partidas ganadas de X: ", n1)
                        print("Partidas ganadas de 0: ", n)
                        print()
                        break

                else:
                    print()
                    print('===ingresa numeros  del 1 al 9====')
                    x=x-1


            x = x+1



        elige = int(input("presiona 1, sino 0 para salir: "))
    os.system("cls")
    salirDelJuego = int(input("Quieres salir del juego:\nVolver a jugar presiona 1, sino 0 para salir: "))
    if salirDelJuego ==0:
        salirJuego()
    #creado por gino loja
