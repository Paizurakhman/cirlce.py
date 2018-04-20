from pygame import *
heigth=640
width=480

init()
screen = display.set_mode((heigth, width))
display.set_caption("Alan`s Animation")

animationTimer = time.Clock()
x=20
y=20
dx=1
dy=0.5

endProgram = False

while not endProgram:
    for e in event.get():
        if e.type == QUIT:
            endProgram = True

    x+=dx
    y+=dy
    if y<0 or y>heigth-200:
        dy*=-1
    if x<0 or x>width+120:
        dx*=-1

    screen.fill((200,250,250))
    draw.ellipse(screen, (0,255,0), (x,y, 40,40))

    animationTimer.tick(1000)
    display.update()
