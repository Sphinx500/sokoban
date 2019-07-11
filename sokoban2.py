#se mueve pero solo imprime una linea
mapa=[
        [2,2,2,2,2],
        [2,4,0,4,2],
        [2,4,4,4,2],
        [2,2,2,2,2]]
#Crea las tablas
j=0
for a in range(len(mapa)):
    print(mapa[j])
    j=j+1
position_row=1
position_col=2
mapa[position_row][position_col]=0
caja=4
while True:
   
    move_row=raw_input("D-right,A-Left,W-Up,S-Down")
tem_row=position_row
tem_col=position_col

if move_row=='d' and mapa[position_row+1]!=2 and map[caja+1]!=2:
    #right
        position_row=position_row+1
elif move_row=='a'and mapa[position_col-1]!=2 and map[caja+1]!=2:
    #left
         position_col=position_col-1
move_col=raw_input("D-right,A-Left,W-Up,S-Down")
if move_col=='w' and mapa[position_col-1]!=2 and map[caja+1]!=2:
    #up
        position_col=position_col-1
elif move_col=='s'and mapa[position_col+1]!=2 and map[caja+1]!=2: 
    #down
         position_col=position_col+1 
mapa[tem_col]=4
mapa[tem_row]=4
mapa[position_col]=0
mapa[position_row]=0
mapa[caja]=4

