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
circlerect = [0]* 9
blockcord = list()
blockrect = list()
for i in range(1,4):
    for j in range(1,4):
        blockcord.append((240*(i - 1) + 120, 240*(j - 1) + 120))
for i in range(9):
    blockrect.append(gridBlock.get_rect(center= (blockcord[i])))
grid =[0]*9
#Game loop
def main():
    while True:
        playerturn = 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            def leftclick():
                if event.type == pg.MOUSEBUTTONDOWN:
                    
                    print("LeftClick")
                    return True
                else:
                    return False
        mouse_pos = pg.mouse.get_pos()
        #Placing cross and circle

        for i in range(9):

            win.blit(gridBlock, blockrect[i])
            if blockrect[i].collidepoint(mouse_pos):
                if leftclick() and playerturn == 1:
                    crossrect[i] = cross.get_rect(center = (blockcord[i]))
                    grid[i] == crossrect[i]
                    playerturn = 0
                    win.blit(cross, crossrect[i])
                elif leftclick() and playerturn == 0:
                    circlerect[i] = circle.get_rect(center = (blockcord[i]))
                    playerturn = 1
                    grid[i] == circlerect[i]
                    win.blit(circle, circlerect[i])
        playerturn = 1
        for i in range(9):
            if crossrect[i] != 0 and playerturn == 1:
                win.blit(cross, crossrect[i])
                playerturn = 0
            if circlerect[i] != 0 and playerturn == 0:
                win.blit(circle,circlerect[i])
                playerturn = 1
        pg.display.update()
        Clock.tick(60)
    
main()