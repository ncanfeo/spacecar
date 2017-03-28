import os,thread,time,sys
#import threading
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
def stop(self):
    self.stopped = True


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
	clear_screen()
	print(str(hp) + "\r")
	print(to_str(border))
	for i in range(height - 1 -(height-line_now)):
		print(to_str(empty_line))
	print(to_str(line_with_spacecar))
	for i in range(height-line_now):
		print(to_str(empty_line))
	print(to_str(border))
'''class Move(threading.Thread):
    def run(self):
        while True:
            keypress()
    def kill(self):
		self.killed = True
		'''
             

if __name__ =='__main__':
	th = thread.start_new_thread(keypress, ())
	while 1:
		if char is not None:
			if char == 'w' and line_now != 1:
				if "*" in empty_line[1:6] :
					hp -= 2
					line_now -= 1
				else:
					line_now -= 1
				char = None
			elif char == 's' and line_now != height:
				if "*" in empty_line[1:6]:
					hp -= 2
					line_now += 1
				else:	
					line_now += 1
				char = None
			elif char == 'q':
				sys.exit()
		i_for_meteorit += 1
		if i_for_meteorit % (spaces_level):
			empty_line.pop(1)
			empty_line.insert(width- 2," ")
		
		else:
			empty_line.pop(1)
			empty_line.insert(width- 2,"*")
		time.sleep(0.25)
		paint_game()
