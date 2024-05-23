from turtle import*
import colorsys
bgcolor('black')
tracer(399)
pensize(3)
h = 1
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(5):
        fd(i*1.2)
        rt(60)
        
        circle(3)
    rt(121)
    end_fill()
done()    
