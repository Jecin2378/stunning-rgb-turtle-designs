from turtle import*
import colorsys
bgcolor('black')
tracer(10000)
pensize(5)
h = 0
for i in range(29999):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(1):
        fd(i*1.2)
        rt(60)
        fd(200)
        rt(120)
        lt(90)
    rt(121)
    end_fill()
done()    