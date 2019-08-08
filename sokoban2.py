"""
0-Personaje
1-Cajas
2-Paredes
3-Metas
4-Pasillos
5-Caja/meta
6-Personaje/Meta
"""

class Sokoban:
    def __init__(self):
        self.maps=[[]]
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
    def crear(self):
        self.maps=[
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,3,4,4,4,4,4,4,4,2],
        [2,4,3,4,4,4,4,4,4,4,3,4,4,4,4,2],
        [2,4,4,4,1,4,4,0,4,4,4,4,1,4,4,2],
        [2,4,4,4,4,4,4,1,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,3,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
        
    def mapa(self):
        
        cont=0
        for cont in range(len(self.maps)):
            print(self.maps[cont])
            cont=cont+1

    def posicion(self):
        for i in range(len(self.maps)):
            for j in range(len(self.maps[i])):
                if self.maps[i][j]==0:
                    self.position_row=i
                    self.position_col=j
                    self.tem_row=self.position_row
                    self.tem_col=self.position_col
#CONTADOR DE CAJAS 
    def cont_cajas (self):
        caja=0
        for x in range(len(self.maps)):
            for y in range(len(self.maps[x])):
                if self.maps[x][y]==1:
                    caja=caja+1
        print("CAJAS RESTANTES ",caja)


#DERECHA
    def derecha(self):
        if self.maps[self.position_row][self.position_col+1]== 4:
            self.position_col=self.position_col+1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_row][self.position_col+1]==1 and self.maps[self.position_row][self.position_col+2]==4: 
            self.position_col=self.position_col+1
            self.caja_col=self.position_col+1
            self.caja_row=self.position_row
            self.maps[self.position_row][self.position_col]=0   
            self.maps[self.tem_row][self.tem_col]=4
            self.maps[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row][self.position_col+1]==5 and self.maps[self.position_row][self.position_col+2]==4:
            self.position_col=self.position_col+1
            self.caja_col=self.caja_col+1
            self.maps[self.position_row][self.position_col]=6 
            self.maps[self.position_row][self.position_col+1]=1
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.maps[self.position_row][self.position_col]==6 and self.maps[self.position_row][self.position_col+1]==1 and self.maps[self.position_row][self.position_col+2]==4:
            self.position_col=self.position_col+1
            self.caja_col=self.caja_col+1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.position_row][self.position_col+1]=1
            self.maps[self.position_row][self.position_col+0]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#meta 
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row][self.position_col+1]==1 and self.maps[self.position_row][self.position_col+2]==3:
             self.position_col=self.position_col+1
             self.maps[self.position_row][self.position_col]=0 
             self.maps[self.position_row][self.position_col+1]=5
             self.maps[self.position_row][self.position_col-1]=4
             self.tem_row=self.position_row
             self.tem_col=self.position_col
           
    
    def izquierda(self):
#IZQUIERDA
        if self.maps[self.position_row][self.position_col-1]== 4:
            self.position_col=self.position_col-1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_row][self.position_col-1]==1 and self.maps[self.position_row][self.position_col-2]==4: 
            self.position_col=self.position_col-1
            self.caja_col=self.position_col-1
            self.caja_row=self.position_row
            self.maps[self.position_row][self.position_col]=0   
            self.maps[self.tem_row][self.tem_col]=4
            self.maps[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row][self.position_col-1]==5 and self.maps[self.position_row][self.position_col-2]==4:
            self.position_col=self.position_col-1
            self.caja_col=self.caja_col-1
            self.maps[self.position_row][self.position_col]=6 
            self.maps[self.position_row][self.position_col-1]=1
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.maps[self.position_row][self.position_col]==6 and self.maps[self.position_row][self.position_col-1]==1 and self.maps[self.position_row][self.position_col-2]==4:
            self.position_col=self.position_col-1
            self.caja_col=self.caja_col-1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.position_row][self.position_col-1]=1
            self.maps[self.position_row][self.position_col+1]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#meta 
        elif self.maps[self.position_row][self.position_col-1]==1 and self.maps[self.position_row][self.position_col-2]==3:
             self.position_col=self.position_col-1
             self.maps[self.position_row][self.position_col]=0 
             self.maps[self.position_row][self.position_col-1]=5
             self.maps[self.position_row][self.position_col+1]=4
             self.tem_row=self.position_row
             self.tem_col=self.position_col


#MOVIMIENTO ARRIBA
    def arriba(self):
        if self.maps[self.position_row-1][self.position_col]== 4:
            self.position_row=self.position_row-1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row-1][self.position_col]==1 and self.maps[self.position_row-2][self.position_col]==4: 
            self.position_row=self.position_row-1
            self.caja_row=self.position_row-1
            self.caja_col=self.position_col
            self.maps[self.position_row][self.position_col]=0 
            self.maps[self.tem_row][self.tem_col]=4
            self.maps[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row-1][self.position_col]==5 and self.maps[self.position_row-2][self.position_col]==4:
            self.position_row=self.position_row-1
            self.caja_row=self.caja_row-1
            self.maps[self.position_row][self.position_col]=6 
            self.maps[self.position_row-1][self.position_col]=1
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.maps[self.position_row][self.position_col]==6 and self.maps[self.position_row-1][self.position_col]==1 and self.maps[self.position_row-2][self.position_col]==4:
            self.position_row=self.position_row-1
            self.caja_row=self.caja_row-1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.position_row-1][self.position_col]=1
            self.maps[self.position_row+1][self.position_col]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        
#meta 
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row-1][self.position_col]==1 and self.maps[self.position_row-2][self.position_col]==3:
             self.position_row=self.position_row-1
             self.maps[self.position_row][self.position_col]=0 
             self.maps[self.position_row-1][self.position_col]=5
             self.maps[self.position_row+1][self.position_col]=4
             self.tem_row=self.position_row
             self.tem_col=self.position_col
    
    def abajo(self):
#ABAJO
        if self.maps[self.position_row+1][self.position_col]==4:
            self.position_row=self.position_row+1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row][self.position_col+1]==1 and self.maps[self.position_row][self.position_col+2]==4: 
            self.position_row=self.position_row+1
            self.caja_col=self.position_col+1
            self.caja_row=self.position_row
            self.maps[self.position_row][self.position_col]=0   
            self.maps[self.tem_row][self.tem_col]=4
            self.maps[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#saca la caja de la meta
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row+1][self.position_col]==5 and self.maps[self.position_row+2][self.position_col]==4:
            self.position_row=self.position_row+1
            self.caja_row=self.caja_row+1
            self.maps[self.position_row][self.position_col]=6 
            self.maps[self.position_row+1][self.position_col]=1
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.maps[self.position_row][self.position_col]==6 and self.maps[self.position_row+1][self.position_col]==1 and self.maps[self.position_row+2][self.position_col]==4:
            self.position_row=self.position_row+1
            self.caja_row=self.caja_row+1
            self.maps[self.position_row][self.position_col]=0
            self.maps[self.position_row-1][self.position_col]=1
            self.maps[self.position_row+1][self.position_col]=3
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#meta 
        elif self.maps[self.position_row][self.position_col]==0 and self.maps[self.position_row+1][self.position_col]==1 and self.maps[self.position_row+2][self.position_col]==3:
             self.position_row=self.position_row+1
             self.maps[self.position_row][self.position_col]=0 
             self.maps[self.position_row-1][self.position_col]=4
             self.maps[self.position_row+1][self.position_col]=5
             self.tem_row=self.position_row
             self.tem_col=self.position_col






    def jugar(self):
        self.crear()
        self.posicion()
        while True:
            self.mapa()
            self.cont_cajas()
            move=raw_input("D-right,A-left,W-up,S-down")
            if move == "d" or move=="D" :
                self.derecha()
            elif move=="a" or move=="A":
                self.izquierda()
            elif move=="s" or move=="S":
                self.abajo()
            elif move=="w" or move=="W":
                self.arriba()
        

sphinx=Sokoban()
sphinx.jugar()

