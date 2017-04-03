Red = '\033[91m'
Green = '\033[92m'
NavyBlue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
End = '\033[0m'
spacecar = [">","0","0",">"]
#spacecar = list("{1}>{2}{0}00{2}{1}>{2}".format(NavyBlue, Red, End))
procent_of_happy_znak = 5
char = None
k = 0
line_now = 2
height = 10
width = 30
border = list(width * "#")
line_with_spacecar = spacecar +list(
                          (width - 4) * " ")
empty_line = list((width) * " ")
i_for_meteorit = 0
hp = 10
spaces_level = 3
line_without_spacecar = []
for i in range(height):
    line_without_spacecar.append(empty_line)
line_without_spacecar.insert(line_now -1 ,line_with_spacecar)
gameover = '''{0}   _____          __  __ ______    ______      ________ _____    _\r
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \  | |\r
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | | |\r
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /  | |\r
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \  |_|\r
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ (_)\r{1}'''.format(
    Yellow, End)
delay = 0.25
znak2 = "@"
game = 1
happy_znak2 = "&"
happy_znak = "{}{}{}".format(Yellow, happy_znak2, End)
znak ="{}{}{}".format(Cyan, znak2, End)
my_score = 0
znaks = []
for i in range((100 // procent_of_happy_znak) -1):
	znaks.append(znak)
znaks.append(happy_znak)
