BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

def clrscr():
    print("\033[2J",end='')

def showcur():
    print("\033[?25h",end='')

def hidecur():
    print("\033[?25l",end='')

def foreground(color):
    print("\033[3",color,"m",end='')

def background(color):
    print("\033[4",color,"m",end='')

def gotoxy(x,y):
    print("\033[",x,";",y,"H",end='')

def putchar(ch):
    if(len(ch) == 1):
        print(ch,end='')
