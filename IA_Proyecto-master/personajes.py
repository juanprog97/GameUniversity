import pygame as pg
from opciones import *
from logica import *
import time
import random

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def xandy(self):
        return self.x, self.y
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.move(dx=-1)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.move(dx=1)
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.move(dy=-1)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.move(dy=1)

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.get_keys()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.blo = y
        self.tempx, self.tempy = -1, -1
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.path = []
        self.cont = 0




    def move(self):
        
        if (self.tempx != self.game.player.x or self.tempy != self.game.player.y) and(self.game.player.y >= self.blo-5 and self.game.player.y <= self.blo+5 ):
            self.cont = 0
            self.tempx, self.tempy = self.game.player.x, self.game.player.y
            tmp = astar((self.x, self.y), (self.game.player.x, self.game.player.y))
            
            if(tmp != False):
                self.path = tmp
              #  print(self.path)
                self.path = self.path + [(self.x, self.y)]
                self.path = self.path[::-1]
            
        elif self.path and self.cont < len(self.path):
            self.x, self.y = self.path[self.cont][0], self.path[self.cont][1]
            
            self.rect.x,self.rect.y = self.x * TILESIZE,self.y * TILESIZE
            self.cont = self.cont + 1
            

       # print(self.rect.x, self.rect.y)
       # print(self.game.player.x, self.game.player.y)
        # for paso in self.path:
        
    def kill(self):
        if((self.x == self.game.player.x) and (self.y == self.game.player.y)):
            return True
        else:
            return False
    def update(self):
        self.move()
       

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN) #verificar si se pueden cambiar los colores de los edificios y los colores del muro
        #O hacer una clase edificio
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class WalllETR(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE) #verificar si se pueden cambiar los colores de los edificios y los colores del muro
        #O hacer una clase edificio
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Point(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.punt
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(VIOLET) #verificar si se pueden cambiar los colores de los edificios y los colores del muro
        #O hacer una clase edificio
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def reor(self):
        while True:
            x =int((random.random() * 81)-1)
            y = int((random.random() * 81)-1)
            if(MAPA[x][y] != '1' and MAPA[x][y] != 'X' ):
                break
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def goal(self):
        if(self.game.player.x == self.x and self.game.player.y == self.y):
            return True
        else:
            return False


