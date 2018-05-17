from Panim import *

x = 5
y = 5

hidecursor()
foreground(RED)
for i in range(5):
    gotoxy(x+i,y)
    putchar('*')
    sleep(.5)
    gotoxy(x+i,y)
    putchar(' ')
    sleep(.5)
input()
foreground(WHITE)
showcursor()
