import curses,os,thread
from time import sleep
from pynput import keyboard
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
char = None
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
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
	char = getch()
thread.start_new_thread(keypress, ())

"""while True:
	if char is not None:
		if char == 'w':
			line += 1
		if char == 's':
			line -= 1"""
"""def on_press(key):
	global line
    if key == keyboard.up:
		line = line + 1
with keyboard.Listener(
        on_press=on_press
        ) as listener:
    listener.join()"""
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
	#stdscr.clear()
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
while 1:
	thread.start_new_thread(keypress, ())
	sleep(1)
	paint_game()
	if char is not None:
		if char == 'w':
			line -= 1
			char = None
		elif char == 's':
			line += 1
			char = None
	#if stdscr.getch():
	#	o = stdscr.getch()
	#	if o == 259 and line != 1:
	#		line -= 1
	#	elif o == 258 and line != lines:
	#		line += 1



