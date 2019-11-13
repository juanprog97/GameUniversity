import pygame as pg
import sys
from os import path
from opciones import *
from personajes import *
from archivoMapa import *
import threading




class Game:
    def __init__(self):
        pg.init()
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        #self.background_image = self.load_image('Mapata.jpg')
        pg.display.set_caption(TITLE)
        myfont = pg.font.SysFont("monospace", 30)
        self.state = False
        self.origenT = myfont.render("Puntaje: ", 30, (255,0,0))
        self.point = myfont.render("0", 30, (255,0,0))
        self.clock = pg.time.Clock()
        self.load_data()

    # def load_image(self,filename, transparent=False):
    #         try: image = pg.image.load(filename)
    #         except pg.error as message:
    #                 raise SystemExit(message)
    #         image = image.convert()
    #         if transparent:
    #                 color = image.get_at((0,0))
    #                 image.set_colorkey(color, RLEACCEL)
    #         return image
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'Mapa.txt'))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.puntaje = 0
        
        self.enemies = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                  #  print(row,col)
                    MAPA[row][col] = 1
                    Wall(self, col, row)
                if tile == 'X':##con esto se identifican que son edificios
                   # print(row,col)
                    MAPA[row][col] = 2##MODIFICAR ESTA PARA RECONOCERLOS A AMBOS
                    WalllETR(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'E':
                    Enemy(self,col,row)

        self.camera = Camera(self.map.width, self.map.height)
        
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        #self.enemy.update()
        self.state = self.enemies.update()
        print(self.state)
        self.player.update()
        #self.state = self.enemies.kill()
        self.camera.update(self.player)
        

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    
    def draw_enemies(self):
         
         for sprite in self.enemies:
            
            self.screen.blit(sprite.image, self.camera.apply(sprite))
         for sprite in self.enemies:
            if(sprite.kill() == True):
                self.playing = False
    def draw(self):
        self.screen.fill(BGCOLOR)
        x,y = self.player.xandy()
        myfont = pg.font.SysFont("monospace", 30)
        self.point = myfont.render(str(self.puntaje), 30, (255,0,0))
        self.screen.blit(self.origenT,(0,0))
        self.screen.blit(self.point,(150,0))
       # self.screen.blit(self.background_image,(0,0))
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        t = threading.Thread(target=self.draw_enemies)
        t.start()
        pg.display.flip()

    def events(self):
        # catch all events here
        # catch all events here
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
