from turtle import*
import colorsys
bgcolor('black')
tracer(1000)
pensize(5)
h = 0
for i in range(2999):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(1):
        fd(i*1.2)
        circle(20)
        rt(40)
        rt(60)
       
    end_fill()
done()    
