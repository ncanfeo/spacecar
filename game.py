import os,time,sys,threading
from random import *
from config import *
"""def lines_do(lines_without_spacecar):
	global liness
	liness = []
	for i in range(line_now -1):
		if lines_without_spacecar:
			liness.append(lines_without_spacecar[0])
			lines_without_spacecar[i].pop(0)
	liness.append(line_with_spacecar)
	for i in range(height - line_now):
		if lines_without_spacecar:
			liness.append(lines_without_spacecar[0])
			lines_without_spacecar[i].pop(0)"""
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
	return "".join(my_list) + "\r"
def clear_screen():
	try:
		os.system('clear')
	except:
		os.system('cls')
def paint_game():
	global k 
	k = 0
	clear_screen()
	print(str(hp) + "\r")
	print(to_str(border))
	for i in range(height - 1 -(height-line_now)):
		print(to_str(line_without_spacecar[i]))
		k += 1
	print(to_str(line_with_spacecar))
	for i in range(height-line_now):
		k += 1
		print(to_str(line_without_spacecar[k]))
		
	print(to_str(border))
def new_meteorit():
	global i_for_meteorit
	i_for_meteorit += 1
	if  i_for_meteorit % (spaces_level):
		for i in range(len(line_without_spacecar)):
			line_without_spacecar[i].pop(1)
			line_without_spacecar[i].insert(width- 2," ")
	else:
		"""z = choice(line_without_spacecar)
		z.pop(1)
		z.insert(width- 2,"*")"""
		z = randint(0,height)
		o = 0
		for i in range(z - 1):
			"""line_without_spacecar[i].pop(1)
			line_without_spacecar[i].insert(width- 2," ")
			o += 1"""
			line_without_spacecar[o]  = line_without_spacecar[o][1:]+[" "]
			o += 1
		"""line_without_spacecar[z].pop(1)
		line_without_spacecar[z].insert(width- 2,"*")"""
		line_without_spacecar[z] = line_without_spacecar[z][1:]+["*"]
		for i in range(height - z):
			"""line_without_spacecar[o].pop(1)
			line_without_spacecar[o].insert(width- 2," ")"""
			
			line_without_spacecar[o]  = line_without_spacecar[o][1:]+[" "]
			o += 1
def proverka_na_simvol():
	global hp,line_now,char
	if char is not None:
			if char == 'w' and line_now != 1:
				if "*" in line_without_spacecar[line_now -1][1:6] :
					hp -= 2
					line_now -= 1
				else:
					line_now -= 1
				char = None
			elif char == 's' and line_now != height:
				if "*" in line_without_spacecar[line_now + 1][1:6]:
					hp -= 2
					line_now += 1
				else:	
					line_now += 1
				char = None
			elif char == 'q':
				sys.exit()
if __name__ =='__main__':
	th = threading.Thread(target=keypress).start()
	while 1:

		#lines_do(lines_without_spacecars)
		proverka_na_simvol()
		new_meteorit()
		paint_game()
		time.sleep(0.25)


