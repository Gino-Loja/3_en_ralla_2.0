from tkinter import *
import random
class SuperVentana:
    """docstring for SuperVentana.
    por ahora solo vale el boton Facil
    """

    def __init__(self):

        self.lista = []
        self.ven = Tk()
        self.listaB = []
        self.puntos = {
            "O": 1
            ,"X": -1
            ,"empate": 0
        }
        self.listaV = [""]*9
        self.elige = True
        self.ven.geometry("500x500")
        self.inicioDelJuego()
        self.ven.mainloop()





    def inicioDelJuego(self):
        #inicio del juego
        frame1 = Frame(self.ven)
        frame1.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        boton1= Button(self.ven,text=("jugar"), width=5,height=5, command = lambda:self.ModoDejuego() )
        boton1.grid(row=0, column=0)
        #salir del juego
        boton2= Button(self.ven,text=("salir"), width=5,height=5,command = lambda:self.colocarFicha(ficha,0,1,2))
        boton2.grid( row=1, column=1)

    def ModoDejuego(self):
        global frame

        frame = Frame(self.ven)
        frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        boton1= Button(frame,text=("Facil"), width=5,height=5, command = lambda:self.jugada() )
        boton1.grid( row=0, column=3,padx=150)
        #salir del juego
        boton2= Button(frame,text=("MEDIO"), width=5,height=5,command = lambda:self.jugada())
        boton2.grid( row=1, column=3)

        boton2= Button(frame,text=("Dificil"), width=5,height=5,command = lambda:self.Dificil())
        boton2.grid( row=2, column=3)



    def botones(self, ficha):

        """self.frame1.place(x = 0, y = 0, relwidth = 1, relheight = 1)"""


        frame.destroy()

        botons= Button(self.ven,text=(""),relief="flat",width=5,height=5, command = lambda:self.colocarFicha(ficha,0,0,1) )
        botons.grid(row=0, column=0)
        self.listaB.append(botons)

        boton2s= Button(self.ven,text=(""), relief="flat",width=5,height=5,command = lambda:self.colocarFicha(ficha,0,1,2))
        boton2s.grid( row=0, column=1)
        self.listaB.append(boton2s)

        boton3s= Button(self.ven,text=(""), relief="flat",width=5,height=5,command = lambda:self.colocarFicha(ficha,0,2,3))
        print(boton3s)
        boton3s.grid( row=0, column=2)
        self.listaB.append(boton3s)

        boton4 = Button(self.ven,text=(""),relief="flat",width=5,height=5,command = lambda:self.colocarFicha(ficha,1,0,4))
        boton4.grid(row=1, column=0)
        self.listaB.append(boton4)

        boton5 = Button(self.ven,text=(""), relief="flat",width=5,height=5,command = lambda:self.colocarFicha(ficha,1,1,5))
        boton5.grid(row=1, column=1)
        self.listaB.append(boton5)

        boton6 = Button(self.ven,text=(""), relief="flat",width=5,height=5,command = lambda:self.colocarFicha(ficha,1,2,6))
        boton6.grid(row=1, column=2)
        self.listaB.append(boton6)

        boton7 = Button(self.ven,text=(""), relief="flat", width=5,height=5,command = lambda:self.colocarFicha(ficha,2,0,7))
        boton7.grid(row=2, column=0)
        self.listaB.append(boton7)

        boton8 = Button(self.ven,text=(""), relief="flat", width=5,height=5,command = lambda:self.colocarFicha(ficha,2,1,8))
        boton8.grid(row=2, column=1)
        self.listaB.append(boton8)

        boton9 = Button(self.ven,text=(""),  relief="flat",width=5,height=5,command = lambda:self.colocarFicha(ficha,2,2,9))
        boton9.grid(row=2, column=2)
        self.listaB.append(boton9)

        self.Lineas()

    def Lineas(self):
        linea = Frame(self.ven, bg = "black")
        linea.place(x = 40, y = 3,width=5, height=250)

        linea2 = Frame(self.ven, bg = "black")
        linea2.place(x = 86, y = 3,width=5, height=251)

        linea3 = Frame(self.ven, bg = "black")
        linea3.place(x = 0, y = 80,width=150, height=5)

        linea4 = Frame(self.ven, bg = "black")
        linea4.place(x = 0, y = 168,width=150, height=5)





    def jugadaMaquina(self):

        n=0

        while True :

            i=0
            num = random.randint(1, 9)

            while i < len(self.lista):
                if self.lista[i] != num:
                   n=n+1

                i=i+1

            if n == len(self.lista):
                k =0
                for i in range(3):
                    for j in  range(3):
                        k +=1
                        if num == k:
                           ia = i
                           ja = j
                           ka = k


                return ia, ja, ka


            elif len(self.lista)==9:
                break
            else:
               posiciom = random.randint(1, 9)

            n=0

            i= 0
        return k




    def Dificil(self):
        self.elige = False
        self.botones('X')



    """ dejo aqui calculo de las posiciones
    aun esta en PROCESO
    """

    def miniMax(self,ma):

        mejor = -float("inf")
        for i in range(9):
            if ma[i]=="":
                ma[i] = self.maquina
                punto = self.minimax(ma,0,False)
                ma[i] = ""
                if punto > mejor:
                    mejor = punto
                    mover = i

        ma[mover] = self.maquina
        return   mover//3,mover%3, mover


    def minimax(self,ma,depth, isMaximizing):
        result,fic  = self.ganador()
        if fic != "":
            return self.puntos[fic]
        if isMaximizing:
            mejor = -float("inf")
            for i in range(9):
                if ma[i]=="":
                    ma[i] = self.maquina
                    punto = self.minimax(ma,depth+1,False)
                    ma[i] = ""
                    # if  iaMaquina == 2:
                    #     mejor = punto
                    # else:
                    mejor = max(punto, mejor)
            return mejor
        else:
            mejor = +float("inf")
            for i in range(9):
                if ma[i]=="":
                    ma[i] = self.fichaJu
                    punto = self.minimax(ma,depth+1,True)
                    ma[i] = ""
                    # if  iaMaquina == 2:
                    #     mejor = punto
                    # else:
                    mejor = min(punto, mejor)
            return mejor


    def jugada(self):

        self.botones("X")


    def colocarFicha(self,ficha, x ,y,posi):

        self.lista.append(posi)
        fichaColocada = Label(self.ven, text=ficha,width=5,height=5,font=("Verdana",10))
        fichaColocada .grid(row= x, column= y)


        for i in range(9):
            if i == posi-1:
                self.listaV[i] = ficha



        ganar,fichaGanadora = self.ganador()


        print(ganar,self.listaV)
        ficha = "O"

        if ficha == "O" and len(self.lista) < 9 and ganar == False:
            self.maquina = "O"
            self.fichaJu = "X"
            if self.elige == False:
                x,y,z = self.miniMax(self.listaV)
                print(x,y,z)


            else:
                x,y,z = self.jugadaMaquina()



            self.lista.append(z)


            # for i in range(9):
            #     if i == z:
            #         self.listaV[i] = ficha


            fichaColocada = Label(self.ven, text=ficha,width=5,height=5,font=("Verdana",10))
            fichaColocada .grid(row= x, column= y)


            ganar,fichaGanadora = self.ganador()

        print('miniMax',ganar,self.listaV)
        if ganar:
            txt= Label(self.ven, text="ganador " + fichaGanadora,width=5,height=5,font=("Verdana",10))
            txt.place(x=50,y=270, width=100, height=30)

            for i in self.listaB:
                i['state'] = DISABLED


            botonretry = Button(self.ven, text=" retry " ,width=5,height=5,font=("Verdana",10), command= lambda:self.retry() )
            botonretry.place(x=50,y=300, width=100, height=30)
            self.boton = botonretry
            self.etiqueta = txt






        self.Lineas()




    def ganador(self):
        ganador = False
        ficha = ''
        #print(self.listaV)
        if self.listaV[0]== self.listaV[4]== self.listaV[8] != "" :
            ganador = True
            return ganador,self.listaV[4]
        elif self.listaV[0]== self.listaV[1]== self.listaV[2] != "":
            ganador = True
            return ganador,self.listaV[1]
        elif self.listaV[3]==self.listaV[4]==self.listaV[5] != "":
            ganador = True
            return ganador,self.listaV[3]
        elif self.listaV[6]== self.listaV[7]==self.listaV[8] != "":
            ganador = True
            return ganador,self.listaV[7]
        elif self.listaV[2]==self.listaV[4]== self.listaV[6] != "":
            ganador = True
            return ganador,self.listaV[4]
        elif self.listaV[0]==self.listaV[3]==self.listaV[6] != "":
            ganador = True
            return ganador,self.listaV[3]
        elif self.listaV[1]==self.listaV[4]== self.listaV[7] != "":
            ganador = True
            return ganador,self.listaV[7]
        elif self.listaV[2]== self.listaV[5]==self.listaV[8] != "":
            ganador = True
            return ganador,self.listaV[5]
        n = 0
        for i  in self.listaV:
            if i != "":
                n+=1

        #print(self.lista)
        if n == 9:
            ganador = True
            ficha = "empate"
            return ganador , ficha

        return ganador, ficha

    def retry(self):
        self.lista = []
        self.listaB = []
        self.listaV = [""]*9
        self.boton.destroy()
        self.etiqueta.destroy()
        self.botones("X")











'''



1 2 3       00 01 02
4 5 6    =  10 11 12
7 8 9       20 21 22


'''













les = SuperVentana()
