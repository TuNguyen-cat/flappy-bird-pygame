import pygame,sys,random
from pygame.locals import *

Windowwidth = 1500
Windowheight = 1000
Background = pygame.image.load('flappy bird.png')

BIRDwidth = 60
BIRDheight = 45
G = 0.5
SPEEDFLY = -8
BIRDIMG = pygame.image.load("flappy bird draw.png")

COLUMNwidth = 60
COLUMNheight = 500
Blank = 160
Distance = 200
COLUMNspeed = 2
COLUMNimg = pygame.image.load('bird bird flappy.png')

class Columns():
    def __init__(self):
        self.width = COLUMNwidth
        self.height = COLUMNheight
        self.blank = Blank
        self.distance = Distance
        self.speed = COLUMNspeed
        self.surface = COLUMNimg
        self.Is = []
        for i in range(3):
            x = i * self.distance
            y = random.randrange(60,Windowheight - self.blank - 60,20)
            self.Is.append([x,y])

    def draw(self):
        for i in range(3):
            DISPLAYSURF.blit(self.surface,(self.Is[i][0],self.Is[i][1] - self.height))
            DISPLAYSURF.blit(self.surface,(self.Is[i][0],self.Is[i][1] + self.blank))

    def update(self):
        for i in range(3):
            self.Is[i][0] -= self.speed
        if self.Is[0][0] < -self.width:
            self.Is.pop(0)
            x = self.Is[1][0] + self.distance
            y = random.randrange(60,Windowheight - self.blank - 60,10)
            self.Is.append([x,y])

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((Windowwidth,Windowheight))
pygame.display.set_caption('Flappy Bird')

class Bird():
    def __init__(self):
        self.width = BIRDwidth
        self.height = BIRDheight
        self.x = (Windowwidth - self.width)/2
        self.y = (Windowheight - self.height)/2
        self.speed = 0
        self.surface = BIRDIMG

    def draw(self):
        DISPLAYSURF.blit(self.surface,(int(self.x),int(self.y)))

    def update(self,mouseClick):
        self.y += self.speed + 0.5 * G
        self.speed += G
        if mouseClick == True:
            self.speed = SPEEDFLY

def main():
    bird = Bird()
    columns = Columns()
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClick = True
        
        DISPLAYSURF.blit(Background,(0,0))
        bird.draw()
        columns.draw()
        bird.update(mouseClick)
        pygame.display.update()
        fpsClock.tick(FPS)
if __name__ == '__main__':
    main()

