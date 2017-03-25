import os,thread,time,sys
#import threading
 

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
char = None
border = []
a = []
line = 2
lines = 3
width = 30
spacecar = [">","0","0",">"]
empty_spacecar = len(spacecar) * ' '
for i in range(width):
	border.append("#")
for i in range(width  - 2):
	a.append(" ")
p  = 0
def keypress():
	global char
	while 1:
		char = getch()
	#th.kill()
thread.start_new_thread(keypress, ())
def clear_screen():
	try:
		os.system('clear')
	except:
		os.system('cls')
def paint_game():
	global p
	p += 1
	if p % (len(spacecar) +1):
		a.pop(0)
		a.append(" ")
	else:
		a.pop(0)
		a.append("*")
	clear_screen()
	border = []
	for i in range(width):
		border.append("#")
	print("".join(border)+"\r")
	for i in range(lines - 1 -(lines-line)):
		print("#"+ "".join(a) +"#\r")
	print("#"+"".join(spacecar) + "".join(a) +"#\r")
	for i in range(lines-line):
		print("#"+ "".join(a) +"#\r")
	print("".join(border)+"\r")
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
		#th = Move()
		#th.start()
		#th = thread.start_new_thread(keypress, ())
		time.sleep(0.25)
		paint_game()
		if char is not None:
			if char == 'w' and line != 1:
				line -= 1
				char = None
			elif char == 's' and line != lines:
				line += 1
				char = None
			elif char == 'q':
				sys.exit()
				
