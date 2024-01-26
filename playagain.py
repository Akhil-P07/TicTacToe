import pygame as pg 
pg.init()
win = pg.display.set_mode((720,720))
Clock = pg.time.Clock()
#Icon and Name
pg.display.set_caption("TicTacToe")
icon = pg.image.load("Icon.png")
pg.display.set_icon(icon)
#Background
bg = pg.Surface((720,720))
bg.fill("black")
#Objects
retrytxt = pg.font.Font("Exo_2\static\Exo2-SemiBold.ttf", 90)
retrytxt = retrytxt.render("RETRY", True, "black")
retrytxtsurface = pg.Surface((300,100))
retrytxtsurface.fill("darkorchid2")
retrytxtsurfacerect = retrytxtsurface.get_rect(center = (360,350))

quittxt = pg.font.Font("Exo_2\static\Exo2-SemiBold.ttf", 90)
quittxt = quittxt.render("QUIT", True, "black")
quittxtsurface = pg.Surface((300,100))
quittxtsurface.fill("darkorchid2")
quittxtsurfacerect = retrytxtsurface.get_rect(center = (360,470))


def playagain(winner):
    end = 0
    gamewinner = pg.font.Font("Exo_2\static\Exo2-SemiBold.ttf", 100)
    if winner == "Draw":
        gamewinner = gamewinner.render("Draw", True, "white")
        g_pos = (200,100)
    elif winner == None:
        gamewinner = gamewinner.render("ERROR!: grid error".format(winner), True, "white")
        g_pos = (200,100)
    else:
        gamewinner = gamewinner.render("Player {} wins".format(winner), True, "white")


    while end == 0:
        win.blit(bg, (0,0))
        win.blit(gamewinner, g_pos)
        win.blit(retrytxtsurface,retrytxtsurfacerect)
        win.blit(retrytxt, (230,295))
        win.blit(quittxtsurface,quittxtsurfacerect)
        win.blit(quittxt, (250,410))
        quittxtsurface.fill("darkorchid2")
        retrytxtsurface.fill("darkorchid2")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        #Mouse hover
        mouse_pos = pg.mouse.get_pos()
        if quittxtsurfacerect.collidepoint(mouse_pos):
            quittxtsurface.fill("darkorchid4")
            if pg.mouse.get_pressed()[0]:
                quittxtsurface.fill("indigo")
                return 0
        elif retrytxtsurfacerect.collidepoint(mouse_pos):
            retrytxtsurface.fill("darkorchid4")
            if pg.mouse.get_pressed()[0]:
                retrytxtsurface.fill("indigo")
                return 1
        pg.display.update()
        Clock.tick(60)