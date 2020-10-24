"""
def tlacidlo(text,vyska,sirka,x,y,farba1,farba2):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x-sirka/2 < mouse[0] < x+sirka/2 and y-vyska/2 < mouse[1] < y+vyska/2:
        pygame.draw.rect(Displej,(farba1),(x-sirka/2,y-vyska/2,sirka,vyska))
        NapisText(text,20,x,y,(0,0,0))
        if click[0] == 1:
            return True
    else:    
        pygame.draw.rect(Displej,(farba2),(x-sirka/2,y-vyska/2,sirka,vyska))
        NapisText(text,20,x,y,(0,0,0))
        return False

def hocaketlacidlo(Nobrazok,Aobrazok,x,y,maska):
    global jedenkratjeden, maskamys
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #maska = pygame.mask.from_surface(Nobrazok)
    offset = (mouse[0]-x,mouse[1]-y)
    print(maska.overlap(maskamys,offset))
    if maska.overlap(maskamys,offset) == None:
        Displej.blit(Nobrazok,(x,y))
        return False
    else:
        Displej.blit(Aobrazok,(x,y))
        if click[0] == 1:
            return True
"""