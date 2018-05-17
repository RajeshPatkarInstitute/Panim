from Panim import *

x = 5
y = 5

clrscr()
hidecursor()
foreground(RED)
background(BLUE)
for i in range(8):
    gotoxy(x+i,y)
    putchar('»')
    sleep(.5)
    gotoxy(x+i,y)
    putchar(' ')
    sleep(.5)
foreground(WHITE)
background(BLACK)
wait()
showcursor()
