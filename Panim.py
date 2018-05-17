from enum import Enum;

class COLOR(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4

def clrscr():
    print("\033[2J", sep='' , end='' , flush=True)

def showcur():
    print("\033[?25h", sep='' , end='' , flush=True)

def hidecur():
    print("\033[?25l", sep='' , end='' , flush=True)

def foreground(color):
    print("\033[3",color,"m", sep='' , end='' , flush=True)

def background(color):
    print("\033[4",color,"m", sep='' , end='' , flush=True)

def gotoxy(x,y):
    print("\033[",x,";",y,"H", sep='' , end='' , flush=True)

def putchar(char):
    if(char.length == 1):
        print(char)

foreground(2);
background(6);
print("HEllo World");
hidecur();
input();
showcur();
clrscr();
print("HEllo Universe");
foreground(9);
background(0);
