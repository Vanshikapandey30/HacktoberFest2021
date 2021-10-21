import turtle
import random
t = turtle.Turtle()
s=turtle.Screen()
list1=['#FF0075','#172774','#77D970']
s.bgcolor('#EDEDED')
t.pencolor('#FF0075')
t.speed(0) 

def makeSq():
  
  i=0
  while i<4:

    t.forward(50)
    t.left(90)

    i=i+1
def pattern():
  j=0
  while(j<75):
    t.pencolor(random.choice(list1))
    j+=1
    makeSq()
    t.right(5)
   
j=0
while(j<8):
  t.pencolor(random.choice(list1))
  j+=1
  pattern()
  t.forward(50)
  t.right(30)


