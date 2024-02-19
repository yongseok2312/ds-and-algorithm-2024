# file: ds26_fractalCircle.py
# desc: 프랙탈 원 그리기

from tkinter import *
import random

def drawCircle(x,y,r):
    
    canvas.create_oval(x-r,y-r, x+r, y+r,width=2, outline=random.choice(colors))

    if r>= 3:
        drawCircle(x-r//2, y , r//2)
        drawCircle(x+r//2, y, r//2)



radius = 400
wSize = 1000
colors = ['red','green','blue', 'black', 'orange','indigo','violet','crimson','gray']

# 메인 함수

window = Tk()
window.title('프랙탈 원그리기')
canvas = Canvas(window, height= 1000 , width= 1000, bg = 'white')
drawCircle(wSize//2, wSize//2, radius)
canvas.pack()
window.mainloop()

