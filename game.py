import os,time,sys,threading
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
	while 1:
		char = getch()	
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
	print("Health: " + str(hp) + "\r")
	print(to_str(border))
	for i in range(height - 1 -(height-line_now)):
		print(to_str(line_without_spacecar[i]))
		k += 1
	print(to_str(line_with_spacecar))
	for i in range(height-line_now):
		print(to_str(line_without_spacecar[k]))
		k += 1
	print(to_str(border))
	print("")
def new_meteorit():
	global i_for_meteorit
	i_for_meteorit += 1
	if  i_for_meteorit % (spaces_level):
		for i in range(len(line_without_spacecar)):
			line_without_spacecar[i]  = line_without_spacecar[i][1:width]+[" "]
	else:
		z = randint(0,height - 1)
		o = 0
		for i in range(z - 1):
			line_without_spacecar[o]  = line_without_spacecar[o][1:width]+[" "]
			o += 1
		line_without_spacecar[z] = line_without_spacecar[z][1:width]+["\033[96m{}\033[0m".format(znak)]
		for i in range(height - z):
			line_without_spacecar[o]  = line_without_spacecar[o][1:width]+[" "]
			o += 1
def proverka_na_simvol():
	global hp,line_now,char
	if char is not None:
				
			if char.lower() == 'w' and line_now != 1:
				if "\033[96m{}\033[0m".format(znak) in line_without_spacecar[line_now -2][1:5] :
					c = 0
					for i in line_without_spacecar[line_now -2][1:5]:
						if i == "\033[96m{}\033[0m".format(znak):
							c += 1
					hp -= 2 * c
					line_without_spacecar[line_now -2][1:5] = " " * 5
					line_now -= 1
				else:
					line_now -= 1
				char = None
			elif char.lower() == 's' and line_now != height:
				if "\033[96m{}\033[0m".format(znak) in line_without_spacecar[line_now -1][1:5]:
					c = 0
					for i in line_without_spacecar[line_now -1][1:5]:
						if i == "\033[96m{}\033[0m".format(znak):
							c += 1
					hp -= 2 * c
					line_without_spacecar[line_now -1][1:5] = " " * 5
					line_now += 1
				else:	
					line_now += 1
				char = None
			elif char == " ":
				pass 
			elif char == 'q':
				sys.exit()
			
if __name__ =='__main__':
	threading.Thread(target=keypress).start()
	while 1:
		if hp < 1:
			clear_screen()
			print(gameover)
			sys.exit()
		proverka_na_simvol()
		new_meteorit()
		paint_game()
		time.sleep(delay)
