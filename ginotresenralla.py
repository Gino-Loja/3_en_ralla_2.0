 
from   colorama  import  init,Fore
init(autoreset = True )
      
import os 

import random 
ma = [""]*9
x = 0

ganador = True

lista = []
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
   
              
             
            
        
       
def Ganador(table,ganador):
     n=0
     l=0 
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
         
     for i in table:
         if i != "":
             n = n+1
             if n==9 and ganador==True:
                print(Fore.YELLOW+"          ###EMPATE####")
                print()
     n=0
     return ganador,f,d  

     

    
    
elige = 1
while elige != 0:
    x=0
    ficha=''
    ganar=True
    lista=[]
    ma=['']*9
    listaGanadora=[]
    fichas=''
    turno=()
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
       maquina = 'X'
              
    turno = (yo,maquina)
    
    while x<9 and ganador:
        

            num=0
            print(lista)
            if turno[x%2]==yo:
                # a = int(input('escoge la posicion: '))
                # print()
                
                a = random.randint(1, 9)
                jugadaMaquina(ma, a)
               
                
                
            else:
                num = random.randint(1, 9)
                jugadaMaquina(ma, num)
                
                
                
                
            print(lista)
            if (a>=1 and a<10)  :
                
                os.system("cls")
                # jugadayo(ma, a)
                ganar,fichas,listaGanadora = Ganador(ma,ganador)
                tablero(ma,listaGanadora,fichas)
                    
                if ganar == False:
                    if fichas==yo:
                        print()
                        print(Fore.RED+"#### ganaste ####")
                        break
                    else:
                        print()
                        print(Fore.BLUE+"#### perdiste ####")
                        break   
                    
            else:
                print()
                print('====ingresa numeros en los parametros establecidos====')
                x=x-1
                
              
            
            
                
            x=x+1    
    if elige == 0:
       break



    




