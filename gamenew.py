#!/usr/bin/env python
import os, time, sys, threading
from random import randint
#config
##############################################################
lines = []
Red = '\033[91m'
Cyan = '\033[96m'
Yellow = '\033[93m'
End = '\033[0m'
spacecar ="{}>00>{}".format(Red,End) #[">","0","0",">"]
char = None
line_now = 2
height = 9
width = 30
border = (width + 2) * "#"
i_for_meteorit = 0
hp = 10
spaces_level = 1
for i in range(height):
    lines.append(list(width * " "))
lines[line_now] = (width) * [" "]
gameover = '''{0}   _____          __  __ ______    ______      ________ _____    _\r
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \  | |\r
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | | |\r
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /  | |\r
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \  |_|\r
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ (_)\r{1}'''.format(Yellow, End)
delay = 0.5
game = True
happy_znak = "&" #"#"{}&{}".format(Yellow,End)
znak =  "#"  #"{}@{}".format(Cyan,End)
my_score = 0
##############################################################
try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def keypress():
    global char
    while game:
        char = getch()

def to_str(my_list):
    return "#" + "".join(my_list) + "#\r"

def score():
    global my_score
    while game:
        my_score += 1
        time.sleep(1)

def clear_screen():
    try:
        os.system('clear')
    except:
        os.system('cls')

def new_meteor():
    global  lines
    if randint(1,20) < 6 :
        for i in lines:
            which_meteor = randint(1, 10)
            if which_meteor == 10:
                i += happy_znak
            elif which_meteor < 6:
                i += znak
            else:
                i += " "
    else:
         for i in lines:
             i += " "

def delete_symvol():
    global lines
    o = 0
    for i in lines:
        if o == line_now:
            i.pop(4)
        else:
            i.pop(0)
        o += 1

def bom():
    global hp
    if znak in lines[line_now][4] :
        hp -= 1
    if happy_znak in lines[line_now][4] :
        hp += 1
def move():
    global hp , line_now , char , game , lines
    if char:
        if char.lower() == 'w' and line_now != 0:
            for i in lines[line_now - 1][0:4]:
                if i == happy_znak:
                    hp += 2
                if i == znak:
                    hp -= 2
            line_now -= 1
            #lines[line_now][4:] = lines[line_now]
            #lines[line_now + 1] = [" ", " ", " ", " "] + lines[line_now]
        elif char.lower() == 's' and line_now != len(lines) -1 :
            for i in lines[line_now + 1][0:4]:
                if i == happy_znak:
                    hp += 2
                if i == znak:
                    hp -= 2
            line_now += 1
            #lines[line_now][4:] = lines[line_now]
            #lines[line_now - 1] = [" "," "," "," "] + lines[line_now]

        elif char == " ":
            pass
        elif char == 'q':
            game = False
        char = None
def paint():
    clear_screen()
    print("Health: " + str(hp) + "  Time: " + str(my_score) + "\r")
    print(border + "\r")
    o = 0
    for i in lines:
        if o != line_now:
            print(to_str(i))
        else:
            print("#"+spacecar  + "".join(i)[4:] + "#\r")
        o += 1
    print(border)

if __name__ == '__main__':
    threading.Thread(target=score).start()
    threading.Thread(target=keypress).start()
    while game:
        if hp < 1:
            game = False
        bom()
        move()
        new_meteor()
        delete_symvol()
        paint()
        time.sleep(delay)
    clear_screen()
    print(gameover)


