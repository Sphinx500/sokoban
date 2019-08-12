import os
import msvcrt

"""
0-Personaje
1-Cajas
2-Muros
3-Metas
4-Pasillos
5-Caja/meta
6-Personaje/Meta
7-Paredes
8-personaje/pared
"""

class Sokoban:
    def __init__(self):
        self.level_1=[[]]
        self.level_2=[[]]
        self.position_row=0
        self.position_col=0
        self.tem_row=0
        self.tem_col=0
        self.caja_row=0
        self.caja_col=0
        self.meta_col=0
        self.meta_row=0
        self.caja1=0
        self.caja2=0
        self.personaje_meta=0
        self.contador_caja=0
        self.caja_lugar=0
        self.con=0
        self.power=0
    
    def crear_1(self):
        self.level_1=[
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,3,1,4,4,0,4,4,1,4,3,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
        
    def mapa_1(self):
        
        cont=0
        for cont in range(len(self.level_1)):
            print(self.level_1[cont])
            cont=cont+1

    def posicion_1(self):
        for i in range(len(self.level_1)):
            for j in range(len(self.level_1[i])):
                if self.level_1[i][j]==0:
                    self.position_row=i
                    self.position_col=j
                    self.tem_row=self.position_row
                    self.tem_col=self.position_col

    def crear_2(self):
        self.level_2=[
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,4,4,4,4,4,4,3,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,1,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,0,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
        
    def mapa_2(self):
        
        cont=0
        for cont in range(len(self.level_2)):
            print(self.level_2[cont])
            cont=cont+1

    def posicion_2(self):
        for i in range(len(self.level_2)):
            for j in range(len(self.level_2[i])):
                if self.level_2[i][j]==0:
                    self.position_row=i
                    self.position_col=j
                    self.tem_row=self.position_row
                    self.tem_col=self.position_col


#DERECHA
    def derecha(self):
        if self.level_1[self.position_row][self.position_col+1]== 4:
            self.position_col=self.position_col+1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.level_1[self.position_row][self.position_col+1]==1 and self.level_1[self.position_row][self.position_col+2]==4: 
            self.position_col=self.position_col+1
            self.caja_col=self.position_col+1
            self.caja_row=self.position_row
            self.level_1[self.position_row][self.position_col]=0   
            self.level_1[self.tem_row][self.tem_col]=4
            self.level_1[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#powerup/caja
        elif self.level_1[self.position_row][self.position_col]==8 and self.level_1[self.position_row][self.position_col+1]==1 and self.level_1[self.position_row][self.position_col+2]==4:
            self.position_col=self.position_col+1
            self.caja_col=self.caja_col+1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.tem_row][self.tem_col]=4
            self.level_1[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row][self.position_col+1]==5 and self.level_1[self.position_row][self.position_col+2]==4:
            self.position_col=self.position_col+1
            self.caja_col=self.caja_col+1
            self.level_1[self.position_row][self.position_col]=6 
            self.level_1[self.position_row][self.position_col+1]=1
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.level_1[self.position_row][self.position_col]==6 and self.level_1[self.position_row][self.position_col+1]==1 and self.level_1[self.position_row][self.position_col+2]==4:
            self.position_col=self.position_col+1
            self.caja_col=self.caja_col+1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.position_row][self.position_col+1]=1
            self.level_1[self.position_row][self.position_col+0]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#meta 
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row][self.position_col+1]==1 and self.level_1[self.position_row][self.position_col+2]==3:
             self.position_col=self.position_col+1
             self.level_1[self.position_row][self.position_col]=0 
             self.level_1[self.position_row][self.position_col+1]=5
             self.level_1[self.position_row][self.position_col-1]=4
             self.tem_row=self.position_row
             self.tem_col=self.position_col
#powerup
    def poder_der(self):
        if self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row][self.position_col+1]==7 and self.level_1[self.position_row][self.position_col+2]==4:
            self.position_col=self.position_col+1
            self.level_1[self.position_row][self.position_col]=8
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#IZQUIERDA

    def izquierda(self):
        if self.level_1[self.position_row][self.position_col-1]== 4:
            self.position_col=self.position_col-1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
            
#mueve la caja
        elif self.level_1[self.position_row][self.position_col-1]==1 and self.level_1[self.position_row][self.position_col-2]==4: 
            self.position_col=self.position_col-1
            self.caja_col=self.position_col-1
            self.caja_row=self.position_row
            self.level_1[self.position_row][self.position_col]=0   
            self.level_1[self.tem_row][self.tem_col]=4
            self.level_1[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row][self.position_col-1]==5 and self.level_1[self.position_row][self.position_col-2]==4:
            self.position_col=self.position_col-1
            self.caja_col=self.caja_col-1
            self.level_1[self.position_row][self.position_col]=6 
            self.level_1[self.position_row][self.position_col-1]=1
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.level_1[self.position_row][self.position_col]==6 and self.level_1[self.position_row][self.position_col-1]==1 and self.level_1[self.position_row][self.position_col-2]==4:
            self.position_col=self.position_col-1
            self.caja_col=self.caja_col-1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.position_row][self.position_col-1]=1
            self.level_1[self.position_row][self.position_col+1]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#meta 
        elif self.level_1[self.position_row][self.position_col-1]==1 and self.level_1[self.position_row][self.position_col-2]==3:
             self.position_col=self.position_col-1
             self.level_1[self.position_row][self.position_col]=0 
             self.level_1[self.position_row][self.position_col-1]=5
             self.level_1[self.position_row][self.position_col+1]=4
             self.tem_row=self.position_row
             self.tem_col=self.position_col
#powerup
    def poder_izq(self):
        if self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row][self.position_col-1]==7 and self.level_1[self.position_row][self.position_col-2]==4:
            self.position_col=self.position_col-1
            self.level_1[self.position_row][self.position_col]=8
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
            

#MOVIMIENTO ARRIBA
    def arriba(self):
        if self.level_1[self.position_row-1][self.position_col]== 4:
            self.position_row=self.position_row-1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row-1][self.position_col]==1 and self.level_1[self.position_row-2][self.position_col]==4: 
            self.position_row=self.position_row-1
            self.caja_row=self.position_row-1
            self.caja_col=self.position_col
            self.level_1[self.position_row][self.position_col]=0 
            self.level_1[self.tem_row][self.tem_col]=4
            self.level_1[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row-1][self.position_col]==5 and self.level_1[self.position_row-2][self.position_col]==4:
            self.position_row=self.position_row-1
            self.caja_row=self.caja_row-1
            self.level_1[self.position_row][self.position_col]=6 
            self.level_1[self.position_row-1][self.position_col]=1
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.level_1[self.position_row][self.position_col]==6 and self.level_1[self.position_row-1][self.position_col]==1 and self.level_1[self.position_row-2][self.position_col]==4:
            self.position_row=self.position_row-1
            self.caja_row=self.caja_row-1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.position_row-1][self.position_col]=1
            self.level_1[self.position_row+1][self.position_col]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        
#meta 
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row-1][self.position_col]==1 and self.level_1[self.position_row-2][self.position_col]==3:
             self.position_row=self.position_row-1
             self.level_1[self.position_row][self.position_col]=0 
             self.level_1[self.position_row-1][self.position_col]=5
             self.level_1[self.position_row+1][self.position_col]=4
             self.tem_row=self.position_row
             self.tem_col=self.position_col
#powerup
    def poder_arriba(self):
        if self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row-1][self.position_col]==7 and self.level_1[self.position_row-2][self.position_col]==4:
            self.position_row=self.position_row-1
            self.level_1[self.position_row][self.position_col]=8
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
    
    def abajo(self):
#ABAJO
        if self.level_1[self.position_row+1][self.position_col]==4:
            self.position_row=self.position_row+1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row][self.position_col+1]==1 and self.level_1[self.position_row][self.position_col+2]==4: 
            self.position_row=self.position_row+1
            self.caja_col=self.position_col+1
            self.caja_row=self.position_row
            self.level_1[self.position_row][self.position_col]=0   
            self.level_1[self.tem_row][self.tem_col]=4
            self.level_1[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row+1][self.position_col]==5 and self.level_1[self.position_row+2][self.position_col]==4:
            self.position_row=self.position_row+1
            self.caja_row=self.caja_row+1
            self.level_1[self.position_row][self.position_col]=6 
            self.level_1[self.position_row+1][self.position_col]=1
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.level_1[self.position_row][self.position_col]==6 and self.level_1[self.position_row+1][self.position_col]==1 and self.level_1[self.position_row+2][self.position_col]==4:
            self.position_row=self.position_row+1
            self.caja_row=self.caja_row+1
            self.level_1[self.position_row][self.position_col]=0
            self.level_1[self.position_row-1][self.position_col]=1
            self.level_1[self.position_row+1][self.position_col]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#meta 
        elif self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row+1][self.position_col]==1 and self.level_1[self.position_row+2][self.position_col]==3:
             self.position_row=self.position_row+1
             self.level_1[self.position_row][self.position_col]=0 
             self.level_1[self.position_row-1][self.position_col]=4
             self.level_1[self.position_row+1][self.position_col]=5
             self.tem_row=self.position_row
             self.tem_col=self.position_col
#powerup
    def poder_abajo(self):
        if self.level_1[self.position_row][self.position_col]==0 and self.level_1[self.position_row+1][self.position_col]==7 and self.level_1[self.position_row+2][self.position_col]==4:
            self.position_row=self.position_row+1
            self.level_1[self.position_row][self.position_col]=8
            self.level_1[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col

#CONTADOR DE CAJAS 
    def cont_cajas1 (self):
        self.caja1=0
        for x in range(len(self.level_1)):
            for y in range(len(self.level_1[x])):
                if self.level_1[x][y]==1:
                    self.caja1=self.caja1+1
        print("CAJAS RESTANTES ",self.caja1)

    def cont_cajas2 (self):
        self.caja2=0
        for x in range(len(self.level_1)):
            for y in range(len(self.level_1[x])):
                if self.level_1[x][y]==1:
                    self.caja2=self.caja2+1
        print("CAJAS RESTANTES ",self.caja2)
        

    def jugarNivel1(self):
        print("WELCOME TO SOKOBAN")
        print("--------------------------------------")
        print("----------NIVEL 1----------")
        print("--------------------------------------")
        print("powers: G-right,J-left,Y-up,H-down ")
        self.crear_1()
        self.posicion_1()
        while True:
            self.mapa_1()
            self.cont_cajas1()
#movimientos
            move1=raw_input("D-right,A-left,W-up,S-down")
            if move1 == "d" or move1=="D" :
                self.derecha()
            elif move1=="a" or move1=="A":
                self.izquierda()
            elif move1=="s" or move1=="S":
                self.abajo()
            elif move1=="w" or move1=="W":
                self.arriba()
            if self.caja1==0:
                print("FELICIDADES,HAS SUPERADO EL NIVEL")
            if self.caja1==0:
                self.con=raw_input("DESEA CONTINUAR?    Y=YES    N=NO")
            if self.con=="Y" or self.con=="y":
                print("CARGANDO SIGUIENTE NIVEL")
                self.jugarNivel2()

#poderes
                self.power=raw_input
            elif move1=="j" or move1=="J":
                self.poder_der()
            elif move1=="g" or move1=="G":
                self.poder_izq()
            elif move1=="y" or move1=="Y":
                self.poder_arriba()
            elif move1=="h" or move1=="H":
                self.poder_abajo()
            os.system("cls")


    def jugarNivel2(self):
        print("--------------------------------------")
        print("----------NIVEL 2----------")
        print("--------------------------------------")
        print("powers: G-right,J-left,Y-up,H-down ")
        self.crear_2()
        self.posicion_2()
        while True:
            self.mapa_2()
            self.cont_cajas2()
#movimientos
            move2=raw_input("D-right,A-left,W-up,S-down")
            if move2 == "d" or move2=="D" :
                self.derecha()
            elif move2=="a" or move2=="A":
                self.izquierda()
            elif move2=="s" or move2=="S":
                self.abajo()
            elif move2=="w" or move2=="W":
                self.arriba()

#poderes
                self.power=raw_input
            elif move2=="j" or move2=="J":
                self.poder_der()
            elif move2=="g" or move2=="G":
                self.poder_izq()
            elif move2=="y" or move2=="Y":
                self.poder_arriba()
            elif move2=="h" or move2=="H":
                self.poder_abajo()
            os.system("cls")


sphinx=Sokoban()
sphinx.jugarNivel1()
sphinx.jugarNivel2()

