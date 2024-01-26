import pygame as pg 
pg.init()
win = pg.display.set_mode((720,720))
Clock = pg.time.Clock()
#Icon and Name
pg.display.set_caption("TicTacToe")
icon = pg.image.load("Icon.png")
pg.display.set_icon(icon)

#Game Objects

gridBlock = pg.transform.smoothscale(pg.image.load("GridBlock.png"), (240,240))
cross = pg.font.Font("Exo_2\static\Exo2-ExtraLight.ttf",240).render("X", True, "Black")
crossrect = [0]* 9
circle = pg.font.Font("Exo_2\static\Exo2-ExtraLight.ttf",240).render("O", True, "Black")
circlerect = [0] * 9
blockcord = list()
blockrect = list()
for i in range(1,4):
    for j in range(1,4):
        blockcord.append((240*(i - 1) + 120, 240*(j - 1) + 120))
for i in range(9):
    blockrect.append(gridBlock.get_rect(center= (blockcord[i])))

#Variables
grid= [False]*9
#Game loop
def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        mouse_pos = pg.mouse.get_pos()
        for i in range(9):
            win.blit(gridBlock, blockrect[i])
            if blockrect[i].collidepoint(mouse_pos):
                if pg.key.get_pressed()[pg.K_x]:                
                    crossrect[i] = cross.get_rect(center = (blockcord[i]))
                elif pg.key.get_pressed()[pg.K_o]:
                    circlerect[i] = circle.get_rect(center = (blockcord[i]))

        for i in range(9):
            if crossrect[i] != 0:
                win.blit(cross, crossrect[i])
            if circlerect[i] != 0:
                win.blit(circle,circlerect[i])
        
        pg.display.update()
        Clock.tick(60)

main()