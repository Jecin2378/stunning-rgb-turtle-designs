from turtle import*
import colorsys
bgcolor('black')
tracer(409)
pensize(3)
h = 1
for i in range(5000):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(1):
        fd(i*1.2)
        lt(60)
        rt(60)
        fd(20)
        rt(120)
        circle(15)
    rt(121)
    end_fill()
done()    
