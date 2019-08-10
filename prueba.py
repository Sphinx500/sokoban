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
        self.caja=0
        self.personaje_meta=0
        self.contador_caja=0
        self.caja_lugar=0
        self.con=0
        self.power=0
    def crear(self):
        self.level_1=[
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,7,4,4,4,4,4,4,2],
        [2,4,4,3,1,4,4,0,7,1,4,4,3,4,4,2],
        [2,4,4,4,4,4,4,1,7,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,3,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
        
    def mapa(self):
        
        cont=0
        for cont in range(len(self.level_1)):
            print(self.level_1[cont])
            cont=cont+1

    def posicion(self):
        for i in range(len(self.level_1)):
            for j in range(len(self.level_1[i])):
                if self.level_1[i][j]==0:
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

    def izquierda(self):
#IZQUIERDA
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
            self.position_col=self.position_col+1
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
#CONTADOR DE CAJAS 
    def cont_cajas (self):
        caja=0
        for x in range(len(self.level_1)):
            for y in range(len(self.level_1[x])):
                if self.level_1[x][y]==1:
                    caja=caja+1
        print("CAJAS RESTANTES ",caja)

#CAMBIO DE NIVEL
        if caja==0:
            print("FELICIDADES,HAS SUPERADO EL NIVEL")
        if caja==0:
            self.con=raw_input("DESEA CONTINUAR?    Y=YES    N=NO")
        if self.con=="Y" or self.con=="y":
            print("CARGANDO SIGUIENTE NIVEL")
        if self.con=="N" or self.con=="n":
            print("GRACIAS POR JUGAR")

    def jugar(self):
        self.crear()
        self.posicion()
        while True:
            self.mapa()
            self.cont_cajas()
            move=raw_input("D-right,A-left,W-up,S-down,")
            if move == "d" or move=="D" :
                self.derecha()
            elif move=="a" or move=="A":
                self.izquierda()
            elif move=="s" or move=="S":
                self.abajo()
            elif move=="w" or move=="W":
                self.arriba()
                self.power=raw_input
            elif move=="j" or move=="J":
                self.poder_der()
            os.system("cls")

sphinx=Sokoban()
sphinx.jugar()

