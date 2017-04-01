Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
End = '\033[0m'
char = None
k = 0
line_now = 2
height = 10
width = 30
border = list(width * "#")
line_with_spacecar = list("{1}>{2}{0}00{2}{1}>{2}".format(Blue,Red,End)+(width - 4)*" " )
empty_line = list( (width)* " " )
i_for_meteorit  = 0
hp = 10
spaces_level  =  1
line_without_spacecar = []
for i in range(height):
	line_without_spacecar.append(empty_line)
lines = []
gameover = '''{0}   _____          __  __ ______    ______      ________ _____    _\r
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \  | |\r
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | | |\r
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /  | |\r
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \  |_|\r
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ (_)\r{1}'''.format(Yellow,End)
delay  = 0.25
znak = "@"
