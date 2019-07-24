"""
0-personaje
1-cajas
2-paredes
3-metas
4-pasillos
5-caja/meta
"""
#definir las instrucciones
class Instructions:
    def __init__(self):
        self.mapa=[]
        self.position_col=0
        self.position_row=0
        self.tem_row=0
        self.tem_col=0
        self.caja_col=0
        #crear el mapa
    def crea_mapa (self):
        self.mapa=[
                [2,2,2,2,2],
                [2,4,0,4,2],
                [2,4,4,4,2],
                [2,2,2,2,2]]
       
#imprimir el mapa
    
    def forma_mapa(self):  
        j=0
        for j in range(len(self.mapa)):
            print(self.mapa[j])
            j=j+1
#encontrar al personaje
    def e_personaje (self):
        for j in range (len(self.mapa)):
            for i in range (len(self.mapa[j])):

                if self.mapa[j][i]==0:
                    self.position_col=j
                    self.position_row=i
                    self.tem_col=self.position_col
                    self.tem_row=self.position_row

#movimiento izquierda
    def move_left (self):
        if self.mapa[self.position_col][self.position_row-1]!=2 and self.mapa[self.position_col][self.position_row-1]!=1:
            self.position_col=self.position_col-1
            self.mapa[self.position_col][self.position_row]=0
            self.mapa[self.tem_row] [self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.mapa[self.position_row][self.position_col-1]!=2 and self.mapa[self.position_row][self.position_col-1]==1: 
            self.position_col=self.position_col-1
            self.caja_col=self.position_col-1
            self.caja_row=self.position_row
#mueve la caja
            self.mapa[self.position_row][self.position_col]=0   
            self.mapa[self.tem_row][self.tem_col]=4
            self.mapa[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#movimiento derecha
    def move_right (self):
        if self.mapa[self.position_col+1]!=2 and self.mapa[self.position_col][self.position_row+1]!=1:
            self.position_col=self.position_col+1
            self.mapa[self.position_col][self.position_row]=0
            self.mapa[self.tem_row][self.tem_row]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.mapa[self.position_row][self.position_col+1]!=2 and self.mapa[self.position_col][self.position_row+1]==1:
            self.position_col=self.position_col+1
            self.caja_col=self.position_col+1
            self.caja_row=self.position_row
#mueve la caja
            self.mapa[self.position_row][self.position_col]=0
            self.mapa[self.tem_row][self.tem_col]=4
            self.mapa[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
 
         
#movimiento arriba
    def move_up (self):
        if self.mapa[self.position_row-1][self.position_col]!=2 and self.mapa[self.position_row-1][self.position_col]!=1:
            self.position_row=self.position_row-1
            self.mapa[self.position_row][self.position_col]=0   #camina arriba
            self.mapa[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.mapa[self.position_row-1][self.position_col]!=2 and self.mapa[self.position_row-1][self.position_col]==1 and self.mapa[self.position_row-2][self.position_col]!=2 and self.mapa[self.position_row-2][self.position_col]!=1: 
            self.position_row=self.position_row-1
            self.caja_row=self.position_row-1
            self.caja_col=self.position_col
#mueve la caja
            self.mapa[self.position_row][self.position_col]=0   
            self.mapa[self.tem_row][self.tem_col]=4
            self.mapa[self.caja_row][self.caja_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col      
#movimiento abajo 
    def move_down (self):
        if self.mapa[self.position_row+1][self.position_col]!=2:
            self.position_row=self.position_row+1
            self.mapa[self.position_row][self.position_col]=0
            self.mapa[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
        elif self.mapa[self.position_row+1][self.position_col]!=2 and self.mapa[self.position_row+1][self.position_col]==1 and self.mapa[self.position_row+2][self.position_col]!=2 and self.mapa[self.position_row+2][self.position_col]!=1: 
            self.position_row=self.position_row+1
            self.caja_row=self.position_row+1
            self.caja_col=self.position_col
#mueve la caja            
            self.mapa[self.position_row] [self.position_col]=0
            self.mapa[self.tem_row][self.tem_col]=4
            self.mapa[self.caja_row][self.tem_col]=1
            self.tem_row=self.position_row
            self.tem_col=self.position_col
#inicio de juego
    def juego (self):
        self.crea_mapa()
        self.forma_mapa()
        self.e_personaje()
        while True:
            self.crea_mapa()
            move=raw_input("D-right,A-Left,W-Up,S-Down")
            if move=='a':
                self.move_left()
            elif move=='d':
                self.move_right()
            elif move=='w':
                self.move_up()
            elif move=='s':
                self.move_down()
sphinx=Instructions()
sphinx.juego()