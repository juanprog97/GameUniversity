MAPA = [[0 for i in range(81)] for i in range(81)]

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (128,0,128)
# game settings
WIDTH = 720   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 20
TITLE = "Javeriana University Game"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE