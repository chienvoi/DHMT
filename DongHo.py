# đồng hồ
import time
import winsound
import turtle
# tạo screen 
wn = turtle.Screen()
wn.bgcolor("#f4ece9")
wn.setup(width=600,height=600)
wn.title("Đồng Hồ đồ họa máy tính")

# tắt animation
wn.tracer(0)
# tạo pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(10)
pen.pensize(3)
#pen.color("#130f40")

# vẽ đồng hồ
def veMatdongho(h, m, s, pen):
    # vẽ viền ngoài
    pen.color("#171715")
    pen.begin_fill()
    pen.up()
    # Di chuyển con rùa đến tọa độ xác định, vẽ một đường thẳng đến đích (x, y) nếu bút hướng xuống và không vẽ nếu bút hướng lên.
    pen.goto(0,220)
    #Quay hướng của rùa thành góc. Dưới đây là một số hướng phổ biến theo độ: 0 (đông), 90 (bắc), 180 (tây), 270 (nam)
    pen.setheading(180)
    pen.pendown()
    pen.circle(220)
    pen.end_fill()
    # vẽ mặt đồng hồ
    pen.color("#e17055","#ffeaa7")
    pen.begin_fill()
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.pendown()
    pen.circle(210)
    pen.end_fill()
    # vẽ giờ
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    for _ in range(12):
        #Đưa rùa về phía trước theo khoảng cách xác định, theo hướng rùa đang hướng tới.
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
      
    for _ in range(60):
        pen.fd(200)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)
     # vẽ kim giờ
    pen.penup()
    pen.goto(0,0)
    pen.color("#341f97") 
    pen.setheading(90)
    goc = (h / 12 *360)
    pen.rt(goc)
    pen.pendown()
    
     # độ dài kim
    pen.fd(100)

      # vẽ kim phút
    pen.penup()
    pen.goto(0,0)
    pen.color("#341f97") 
    pen.setheading(90)
    goc = (m / 60 *360)
    pen.rt(goc)
    pen.pendown()
     # độ dài kim
    pen.fd(130)

     # vẽ kim giây
    pen.penup()
    pen.goto(0,0)
    pen.color("#341f97") 
    pen.setheading(90)
    goc = (s / 60 *360)
    pen.rt(goc)
    pen.pendown()
     # độ dài kim
    pen.fd(150)
    # số 1
    pen.penup()
    pen.goto(0,0)
    pen.setheading(60)
    pen.fd(160)
    pen.write(1,font=("Arial",15,"normal"))     
     # số 2
    pen.penup()
    pen.goto(0,0)
    pen.setheading(28)
    pen.fd(165)
    pen.write(2,font=("Arial",15,"normal")) 
     # số 3
    pen.penup()
    pen.goto(0,0)
    pen.setheading(356)
    pen.fd(170)
    pen.write(3,font=("Arial",15,"normal")) 
     # số 4
    pen.penup()
    pen.goto(0,0)
    pen.setheading(326)
    pen.fd(180)
    pen.write(4,font=("Arial",15,"normal")) 
     # số 5
    pen.penup()
    pen.goto(0,0)
    pen.setheading(298)
    pen.fd(182)
    pen.write(5,font=("Arial",15,"normal")) 
     # số 6
    pen.penup()
    pen.goto(0,0)
    pen.setheading(269)
    pen.fd(185)
    pen.write(6,font=("Arial",15,"normal")) 
     # số 7
    pen.penup()
    pen.goto(0,0)
    pen.setheading(242)
    pen.fd(182)
    pen.write(7,font=("Arial",15,"normal")) 
     # số 8
    pen.penup()
    pen.goto(0,0)
    pen.setheading(212)
    pen.fd(185)
    pen.write(8,font=("Arial",15,"normal")) 
     # số 9
    pen.penup()
    pen.goto(0,0)
    pen.setheading(184)
    pen.fd(175)
    pen.write(9,font=("Arial",15,"normal")) 
     # số 10
    pen.penup()
    pen.goto(0,0)
    pen.setheading(155)
    pen.fd(170)
    pen.write(10,font=("Arial",15,"normal")) 
     # số 11
    pen.penup()
    pen.goto(0,0)
    pen.setheading(122)
    pen.fd(160)
    pen.write(11,font=("Arial",15,"normal")) 
     # số 12
    pen.penup()
    pen.goto(0,0)
    pen.setheading(93)
    pen.fd(160)
    pen.write(12,font=("Arial",15,"normal")) 
while True:    
    h = int(time.strftime("%H"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    tanso = 380  
    thoigian = 950
    winsound.Beep(tanso, thoigian)
    veMatdongho(h,m,s,pen)
    wn.update()
    # mượt hơn
   # time.sleep(0.95)
     # clear nét vẽ của giây trước
    pen.clear()
#wn.mainloop()