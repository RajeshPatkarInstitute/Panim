## <img src="Panim.svg"/> 
### <img src="https://img.shields.io/github/license/mashape/apistatus.svg?longCache=true&style=for-the-badge"/> 
### A Library that enables character based console animation

## Installation
> Requires `Python` and currently tested and supported on `MacOSX` and `Linux`
### 1. Donwload the `latest` release of [Panim.py](https://github.com/archanpatkar/Panim/releases/tag/0.1)
### 2. Add the `Panim.py` in your Project folder
### 3. Now you can use `Panim` in your Project

## Example Usage
```python
from Panim import *

x = 5
y = 5

clrscr()
hidecursor()
foreground(RED)
background(BLUE)
for i in range(10):
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
```
For Complete Reference - [API](https://github.com/archanpatkar/Panim/wiki/API-Reference)

### Made with ❤️ in  🇮🇳
