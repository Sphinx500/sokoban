mapa=[
        [2,2,2,2,2],
        [2,4,0,4,2],
        [2,4,4,4,2],
        [2,2,2,2,2]]
#FUNCIONA
j=0
for a in range(len(mapa)):
    print(mapa[j])
    j=j+1


#intento 1:sigue marca error (he buscado en internet sin exito)
"""
for var in mapa:
    for var in jar:
        print(var, end=', ')
"""
#intento 2: Funciona pero se debe hacer de forma manual
"""
print (mapa[1])
print (mapa[2])
print (mapa[3])
"""

#codigo de movimientos
position_row=1
position_col=2
while True:
    print(mapa)
    move_row=raw_input("D-right,A-Left")
tem_row=position_row
if move_row=='d' and mapa[position_row+1]!=2:
    #right
        position_row=position_row+1
elif move_row=='a'and mapa[position_col-1]!=2:
    #left
         position_col=position_col-1
tem_col=position_col
move_col=raw_input("W-Up,S-Down")
if move_col=='w' and mapa[position_col-1]!=2:
    #right
        position_col=position_col-1
elif move_col=='s'and mapa[position_col+1]!=2:
    #left
         position_col=position_col+1