from turtle import*
import colorsys
bgcolor('black')
tracer(10)
pensize(5)
h = 0
for i in range(50000):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor(c)
    fillcolor(c)
    begin_fill()
    for j in range(5):
        fd(200)
        lt(144)
    hideturtle()
   
    
   
    
    
    end_fill()
done()    
