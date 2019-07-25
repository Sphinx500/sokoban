class Game:
    def __init__(self):
        self.maps=[[]]
        self.position_row=0
        self.position_col=0
        self.tem_row=0
        self.tem_col=0
        self.caja_row=0
        self.caja_col=0
    def crear(self):
        self.maps=[
        [2,2,2,2,2,2,2,2,2,2,2,2],
        [2,4,4,4,4,4,4,4,4,4,4,2],
        [2,0,1,4,4,1,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,2],
        [2,4,4,4,4,4,4,4,4,4,4,2],
        [2,2,2,2,4,4,4,4,4,4,4,2]]
       
#imprimir el mapa
    
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

#IZQUIERDA
    def move_left (self):
        if self.maps[self.position_row][self.position_col-1]!=2 and self.maps[self.position_row][self.position_col-1]!=1:
            self.position_col=self.position_col-1
            self.maps[self.position_row][self.position_col]=0   
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
            
        elif self.maps[self.position_row][self.position_col-1]!=2 and self.maps[self.position_row][self.position_col-1]==1 and self.maps[self.position_row][self.position_col-2]!=2 and self.maps[self.position_row][self.position_col-2]!=1: 
            """
            self.position_col=self.position_col-1
            self.caja_col=self.position_col-1
            self.caja_row=self.position_row
            """
#DERECHA
    def move_right (self):
        if self.maps[self.position_col+1]!=2 and self.maps[self.position_row][self.position_col+1]!=1:
            self.position_col=self.position_col+1
            self.maps[self.position_col][self.position_row]=0
            self.maps[self.tem_row][self.tem_col]=4
            self.tem_row=self.position_row
            self.tem_col=self.position_col
     
        elif self.maps[self.position_row][self.position_col+1]!=2 and self.maps[self.position_col][self.position_row+1]==1:
           self.position_col=self.position_col+1
           """                      
            self.caja_col=self.position_col+1
            self.caja_row=self.position_row
        """
    def jugar(self):
        self.crear()
        self.posicion()
        while True:
            self.mapa()
            move=raw_input("D-right,A-left,W-up,S-down")
            if move == "d" or move=="D" :
                self.move_right()
            elif move=="a" or move=="A":
                self.move_left()

sphinx=Game()
sphinx.jugar()


