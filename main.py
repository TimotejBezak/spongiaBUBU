import pygame, time, math, random

pygame.init()

Displej = pygame.display.set_mode((1500, 780))
pygame.display.set_caption('super hra')

Hodiny = pygame.time.Clock()

#load obrazkov
mriezka = pygame.image.load('mriezka.png')
jedenkratjeden = pygame.image.load('jedenkratjeden.png')
divnetlacidlo = pygame.image.load('divnetlacidlo.png')
maskamys = pygame.mask.from_surface(jedenkratjeden)
maskamys.fill()
# konstanty


#smoothscaleobrazkov - pygame.transform.smoothscale(obrazok,(sirka,vyska))


#region funkcie
def prefarb(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def NapisText(co,velkost,xposstredu,yposstredu,farba):
    Fond = pygame.font.Font('freesansbold.ttf', velkost)
    textSurface = Fond.render(co, True, farba)
    TextSurf, TextRect = (textSurface, textSurface.get_rect())
    TextRect.center = (xposstredu, yposstredu)
    Displej.blit(TextSurf, TextRect)
#endregion

#region classy
class tlacidlo:
    global maskamys, poziciamyse, click
    def __init__(self,Nobrazok,Aobrazok,x,y):
        self.Nobrazok = Nobrazok
        self.Aobrazok = Aobrazok
        self.x = x
        self.y = y
        self.maska = pygame.mask.from_surface(Nobrazok)
    def update(self):
        
        #maska = pygame.mask.from_surface(Nobrazok)
        offset = (poziciamyse[0]-self.x,poziciamyse[1]-self.y)
        #print(self.maska.overlap(maskamys,offset))
        if self.maska.overlap(maskamys,offset) == None:
            Displej.blit(self.Nobrazok,(self.x,self.y))
            return False
        else:
            Displej.blit(self.Aobrazok,(self.x,self.y))
            if click[0] == 1:
                return True
#endregion

poziciamyse = 0
click = 0
def pravidla():
    global poziciamyse, click
    stop=False
    tlacidlo8 = tlacidlo(divnetlacidlo,mriezka,200,200)
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
        poziciamyse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        Displej.fill((255,255,0))
        if tlacidlo8.update() == True:
            gameloop()
        pygame.display.update()
        Hodiny.tick(20)

stlaceneKlavesi = []
def gameloop():
    global stlaceneKlavesi, poziciamyse, click

    Xstlacene = False
    while not Xstlacene:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Xstlacene = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    stlaceneKlavesi.append('w')
                if event.key == pygame.K_a:
                    stlaceneKlavesi.append('a')
                if event.key == pygame.K_s:
                    stlaceneKlavesi.append('s')
                if event.key == pygame.K_d:
                    stlaceneKlavesi.append('d')
                if event.key == pygame.K_ESCAPE:
                    Xstlacene = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w and 'w' in stlaceneKlavesi:
                    stlaceneKlavesi.remove('w')
                if event.key == pygame.K_a and 'a' in stlaceneKlavesi:
                    stlaceneKlavesi.remove('a')
                if event.key == pygame.K_s and 's' in stlaceneKlavesi:
                    stlaceneKlavesi.remove('s')
                if event.key == pygame.K_d and 'd' in stlaceneKlavesi:
                    stlaceneKlavesi.remove('d')


        #nejakazmena
        poziciamyse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        Displej.fill((0,255,0))
        NapisText('bubu',20,200,200,(0,0,0))
        pygame.display.update()
        Hodiny.tick(60)
    pygame.quit()

pravidla()