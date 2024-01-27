import pygame as pg 
from TicTacToe import main
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
#Main menu objects
headertxt = pg.transform.smoothscale(pg.image.load("Logo.png"),(642,142))
playtxt = pg.font.Font("Exo_2\static\Exo2-SemiBold.ttf", 90)
playtxt = playtxt.render("PLAY", True, "black")
playtxtsurface = pg.Surface((300,100))
playtxtsurface.fill("darkorchid2")
playtxtsurfacerect = playtxtsurface.get_rect(center = (360,490))

quittxt = pg.font.Font("Exo_2\static\Exo2-SemiBold.ttf", 90)
quittxt = quittxt.render("QUIT", True, "black")
quittxtsurface = pg.Surface((300,100))
quittxtsurface.fill("darkorchid2")
quittxtsurfacerect = playtxtsurface.get_rect(center = (360,610))



bgmusic = pg.mixer.Sound("y2mate.com - Single Player Menu  Mario Kart 7.mp3")

volumetxt = pg.font.Font("Exo_2\static\Exo2-SemiBold.ttf", 20)
bgmusic.play(-1)
print("Controls:\nm to mute \ndown arrow - reduce volume\nup arrow - increase volume\n X - place X cross \n O - place O circle ")
def menuMain():
    volume = 0.3
    while True:
        win.blit(bg,(0,0))
        win.blit(headertxt,(50,200))
        win.blit(playtxtsurface,playtxtsurfacerect)
        win.blit(playtxt, (250,435))
        win.blit(quittxtsurface,quittxtsurfacerect)
        win.blit(quittxt, (250,545))
        win.blit(volumetxt.render("Volume: " + str(int((round(volume* 10) * 10))) +"%", True, "purple"), (590, 0) )

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            #Volume of music 
            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_DOWN]:
                    volume -= 0.1
                elif pg.key.get_pressed()[pg.K_UP]:
                    volume += 0.1
                elif pg.key.get_pressed()[pg.K_m]:
                    volume = 0
        
        #Volume limits
        if volume > 1:
            volume = 1
        elif volume < 0:
            volume = 0
        bgmusic.set_volume(volume)

        #Mouse hover
        mouse_pos = pg.mouse.get_pos()
        if quittxtsurfacerect.collidepoint(mouse_pos):
            quittxtsurface.fill("darkorchid4")
            if pg.mouse.get_pressed()[0]:
                quittxtsurface.fill("indigo")
                return 0
        elif playtxtsurfacerect.collidepoint(mouse_pos):
            playtxtsurface.fill("darkorchid4")
            if pg.mouse.get_pressed()[0]:
                playtxtsurface.fill("indigo")
                return 1          
        else:
            quittxtsurface.fill("darkorchid2")
            playtxtsurface.fill("darkorchid2")
        pg.display.update()
        Clock.tick(120)