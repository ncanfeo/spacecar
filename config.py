char = None
k = 0
line_now = 2
height = 10
width = 30
border = list(width * "#")
line_with_spacecar = list(">00>"+(width - 4)*" " )
empty_line = list( (width)* " " )
i_for_meteorit  = 0
hp = 2
spaces_level  = 5
line_without_spacecar = []
for i in range(height):
	line_without_spacecar.append(empty_line)

lines = []
gameover = '''   _____          __  __ ______    ______      ________ _____    _\r
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \  | |\r
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | | |\r
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /  | |\r
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \  |_|\r
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ (_)\r'''
