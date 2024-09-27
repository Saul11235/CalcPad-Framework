# string generator

nro_data=20

#   #def SVG_line2$(draw_X1$; draw_Y1$; draw_X2$; draw_Y2$)
#   #val
#   #show
#   '<polyline points="'SVG_pointerX','SVG_pointerY' 'SVG_pointerX + (draw_X1$)*SVG_scaleFactor','SVG_pointerY + (draw_Y1$)*SVG_scaleFactor'  'SVG_pointerX + (draw_X1$ + draw_X2$)*SVG_scaleFactor','SVG_pointerY + (draw_Y1$ + draw_Y2$)*SVG_scaleFactor'" style="stroke:'SVG_getcolorLine$'; stroke-width:'SVG_LineWidth'; fill:none; stroke-opacity:'SVG_LineOpacity'" />
#   #val
#   #hide
#   SVG_storageX = draw_X1$ + draw_X2$
#   SVG_storageY = draw_Y1$ + draw_Y2$
#   SVG_move$(SVG_storageX ; SVG_storageY)
#   #end def


def get_punto(order):
    EqX="SVG_pointerX + ("
    EqY="SVG_pointerY + ("
    l=[];ll=[]
    for x in range(order+1):
        l.append("draw_X"+str(int(x+1))+"$")
        ll.append("draw_Y"+str(int(x+1))+"$")
    EqX+="+".join(l)
    EqY+="+".join(ll)
    EqX+=")*SVG_scaleFactor"
    EqY+=")*SVG_scaleFactor"
    punto="'"+EqX+"','"+EqY+"'"
    return punto


def get_code(order):
    strorder=str(int(order))
    code="#def SVG_line"+strorder+"$("
    l=[]
    for x in range(order):
        l.append("draw_X"+str(int(x+1))+"$")
        l.append("draw_Y"+str(int(x+1))+"$")
    code+="; ".join(l)+")\n  #val\n  #show\n  "
    code+="""'<polyline points="'SVG_pointerX','SVG_pointerY' """
    puntos=[]
    for x in range(order): puntos.append(get_punto(x))
    code+=" ".join(puntos)
    code+=""" " style="stroke:'SVG_getcolorLine$'; stroke-width:'SVG_LineWidth'; fill:none; stroke-opacity:'SVG_LineOpacity'" />"""

    code+="\n  #val\n  #hide"
    l=[];ll=[]
    for x in range(order):
        l.append("draw_X"+str(int(x+1))+"$")
        ll.append("draw_Y"+str(int(x+1))+"$")
    code+="\n  SVG_storageX = "+" + ".join(l)
    code+="\n  SVG_storageY = "+" + ".join(ll)
    code+="\n  SVG_move$(SVG_storageX ; SVG_storageY)\n#end def"
    return code

all_code=[]
for x in range(nro_data):
    all_code.append(get_code(x+1))
strcode="\n".join(all_code)

print(strcode)

f=open("./generated.txt","w")
f.write(strcode)
f.close()
print("finished!")

