"""
0-personaje
1-cajas
2-paredes
3-metas
4-pasillos
5-caja/meta
"""

map=[2,4,4,4,0,4,4,4,2]
position_x=4

while True:
    print (map)
    move=raw_input("D-right,A-Left")
    tem_x=position_x
    #tem_x guarda la posicion ddel personaje
    if move=='d' and map[position_x+1]!=2:
        position_x=position_x+1
    elif move=='a':
         position_x=position_x-1
    map[tem_x]=4
    map[position_x]=0