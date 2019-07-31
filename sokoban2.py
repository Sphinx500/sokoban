"""
0-Personaje
1-Cajas
2-Paredes
3-Metas
4-Pasillos
5-Caja/meta
"""
class Sokoban:
    def __init__(self):
        self.maps=[[]]
        self.position_raw=0
        self.position_col=0
        self.tem_raw=0
        self.tem_col=0
        self.caja_raw=0
        self.caja_col=0
    def crear(self):
        self.maps=[
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,1,4,4,4,4,4,4,4,4,4,3,2],
        [2,4,0,4,4,4,4,4,4,4,4,4,4,4,4,2],
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
                    self.position_raw=i
                    self.position_col=j
                    self.tem_raw=self.position_raw
                    self.tem_col=self.position_col


    def derecha(self):
#DERECHA
        if self.maps[self.position_raw][self.position_col+1]!=2 and self.maps[self.position_raw][self.position_col+1]!=1:
            self.position_col=self.position_col+1
            self.maps[self.position_raw][self.position_col]=0
            self.maps[self.tem_raw][self.tem_col]=4
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_raw][self.position_col+1]!=2 and self.maps[self.position_raw][self.position_col+1]==1 and self.maps[self.position_raw][self.position_col+2]!=2 and self.maps[self.position_raw][self.position_col+2]!=1 : 
            self.position_col=self.position_col+1
            self.caja_col=self.position_col+1
            self.caja_raw=self.position_raw
            self.maps[self.position_raw][self.position_col]=0   
            self.maps[self.tem_raw][self.tem_col]=4
            self.maps[self.caja_raw][self.caja_col]=1
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col
#meta 
        elif self.maps[self.position_raw][self.position_col+1]==1 and self.maps[self.position_raw][self.position_col+2]==3 and self.maps[self.position_raw][self.position_col+2]!=2:
             self.position_col=self.position_col+1
             self.caja_col=self.position_col+1
             self.caja_raw=self.position_raw
             self.maps[self.tem_raw][self.tem_col]=0
             self.maps[self.position_col][self.position_raw]=5
             self.tem_col=self.position_col
    
    def izquierda(self):
#IZQUIERDA
        if self.maps[self.position_raw][self.position_col-1]!=2 and self.maps[self.position_raw][self.position_col-1]!=1:
            self.position_col=self.position_col-1
            self.maps[self.position_raw][self.position_col]=0   
            self.maps[self.tem_raw][self.tem_col]=4
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_raw][self.position_col-1]!=2 and self.maps[self.position_raw][self.position_col-1]==1 and self.maps[self.position_raw][self.position_col-2]!=2 and self.maps[self.position_raw][self.position_col-2]!=1: 
            self.position_col=self.position_col-1
            self.caja_col=self.position_col-1
            self.caja_raw=self.position_raw
            self.maps[self.position_raw][self.position_col]=0   
            self.maps[self.tem_raw][self.tem_col]=4
            self.maps[self.caja_raw][self.caja_col]=1
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col
        #meta 
        elif self.maps[self.position_raw][self.position_col-1]==1 and self.maps[self.position_raw][self.position_col-2]==3 and self.maps[self.position_raw][self.position_col-2]!=2:
             self.position_col=self.position_col-1
             self.caja_col=self.position_col+1
             self.caja_raw=self.position_raw
             self.maps[self.tem_raw][self.tem_col]=0
             self.maps[self.position_col][self.position_raw]=5
             self.tem_col=self.position_col

    def arriba(self):
        if self.maps[self.position_raw-1][self.position_col]!=2 and self.maps[self.position_raw-1][self.position_col]!=1:
            self.position_raw=self.position_raw-1
            self.maps[self.position_raw][self.position_col]=0
            self.maps[self.tem_raw][self.tem_col]=4
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_raw-1][self.position_col]!=2 and self.maps[self.position_raw-1][self.position_col]==1 and self.maps[self.position_raw-2][self.position_col]!=2 and self.maps[self.position_raw-2][self.position_col]!=1: 
            self.position_raw=self.position_raw-1
            self.caja_raw=self.position_raw-1
            self.caja_col=self.position_col
            self.maps[self.position_raw][self.position_col]=0 
            self.maps[self.tem_raw][self.tem_col]=4
            self.maps[self.caja_raw][self.caja_col]=1
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col      
    
    def abajo(self):
#ABAJO
        if self.maps[self.position_raw+1][self.position_col]!=2 and self.maps[self.position_raw+1][self.position_col]!=1:
            self.position_raw=self.position_raw+1
            self.maps[self.position_raw][self.position_col]=0   
            self.maps[self.tem_raw][self.tem_col]=4
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col
#mueve la caja
        elif self.maps[self.position_raw+1][self.position_col]!=2 and self.maps[self.position_raw+1][self.position_col]==1 and self.maps[self.position_raw+2][self.position_col]!=2 and self.maps[self.position_raw+2][self.position_col]!=1: 
            self.position_raw=self.position_raw+1
            self.caja_raw=self.position_raw+1
            self.caja_col=self.position_col
            self.maps[self.position_raw][self.position_col]=0 
            self.maps[self.tem_raw][self.tem_col]=4
            self.maps[self.caja_raw][self.caja_col]=1
            self.tem_raw=self.position_raw
            self.tem_col=self.position_col 
                               
    def jugar(self):
        self.crear()
        self.posicion()
        while True:
            self.mapa()
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

