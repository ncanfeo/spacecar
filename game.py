import os, time, sys, threading
from random import *
from config import *
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

def score():
    global my_score
    while game:
        my_score += 1
        time.sleep(1)

def to_str(my_list):
    return "#" + "".join(my_list) + "#\r"


def clear_screen():
    try:
        os.system('clear')
    except:
        os.system('cls')


def paint_game():
        k = 0
        clear_screen()
        print("Health: " + str(hp) + "  Time: " + str(my_score) + "\r")
        print(to_str(border))
        for i in range(len(line_without_spacecar)):
            print(to_str(line_without_spacecar[i]))
        print(to_str(border))
        print("")


def new_meteorit():
    global i_for_meteorit
    i_for_meteorit += 1
    if i_for_meteorit % (spaces_level):
        for i in range(len(line_without_spacecar)):
            if i == line_now - 1:
                line_without_spacecar[
                    i] = spacecar + line_without_spacecar[i][5:width] + [" "]
            else:
                line_without_spacecar[
                    i] = line_without_spacecar[i][1:width] + [" "]

    else:
        z = randint(0, height)
        o = 0
        for i in range(z - 1):
            if z != line_now - 1:
                line_without_spacecar[
                    o] = line_without_spacecar[o][1:width] + [" "]
                o += 1
            else:
                line_without_spacecar[
                    o] = spacecar + line_without_spacecar[o][5:width] + [" "]
                o += 1
        if z != line_now - 1:
            line_without_spacecar[
                z] = line_without_spacecar[z][1:width] + [choice(znaks)]
            o += 1
        else:
            line_without_spacecar[
                z] = spacecar + line_without_spacecar[z][5:width] + [choice(znaks)]
            o += 1
        for i in range(height - z):
            if o != line_now - 1:
                line_without_spacecar[
                    o] = line_without_spacecar[o][1:width] + [" "]
                o += 1
            else:
                line_without_spacecar[
                    o] = spacecar + line_without_spacecar[o][5:width] + [" "]
                o += 1


def proverka_na_simvol():
    global hp, line_now, char, game
    if char is not None:

        if char.lower() == 'w' and line_now != 1:
            c = 0
            for i in line_without_spacecar[line_now - 2][1:4]:
                if i == znak:
                    c += 1
                if i == happy_znak:
                    c -= 1
            hp -= 2 * c
            line_without_spacecar[line_now - 1] = [
                " ", " ", " ", " ", " "
            ] + line_without_spacecar[line_now - 1][5:width]
            line_without_spacecar[
                line_now -
                2] = spacecar + line_without_spacecar[line_now -
                                                      2][5:width] + [" "]
            line_now -= 1
            char = None
        elif char.lower() == 's' and line_now != height + 1:
            #if spacecar in line_without_spacecar[line_now - 1][1:5]:
            c = 0
            for i in line_without_spacecar[line_now][1:4]:
                if i == znak:
                    c += 1
                if i == happy_znak:
                    c -= 1
            hp -= 2 * c
            line_without_spacecar[line_now - 1] = [
                " ", " ", " ", " ", " "
            ] + line_without_spacecar[line_now - 1][5:width]
            line_without_spacecar[
                line_now] = spacecar + line_without_spacecar[line_now][5:
                                                                       width] + [
                                                                           " "
                                                                       ]
            line_now += 1
            char = None
        elif char == " ":
            pass
        elif char == 'q':
            game = 0
    if znak in line_without_spacecar[line_now -1][5] :
        hp -= 1
        line_without_spacecar[line_now -1][5] = " "
    if happy_znak in line_without_spacecar[line_now -1][5] :
        hp += 1
        line_without_spacecar[line_now -1][5] = " "
    

if __name__ == '__main__':
    threading.Thread(target=score).start()
    threading.Thread(target=keypress).start()
    # threading.Thread(target=paint_game).start()
    while game:
        if hp < 1:
            game = 0
        proverka_na_simvol()
        new_meteorit()
        paint_game()
        time.sleep(delay)
    clear_screen()
    print(gameover)
