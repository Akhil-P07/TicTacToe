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
crossrect = [(-200,-200)]* 9
circle = pg.font.Font("Exo_2\static\Exo2-ExtraLight.ttf",240).render("O", True, "Black")
circlerect = [(-200,-200)]* 9
blockcord = list()
blockrect = list()
for i in range(1,4):
    for j in range(1,4):
        blockcord.append((240*(i - 1) + 120, 240*(j - 1) + 120))
for i in range(9):
    blockrect.append(gridBlock.get_rect(center= (blockcord[i])))

#Variables
grid= [[0,0]]*9
winpos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], [2, 1, 0], [5, 4, 3], [8, 7, 6], [6, 3, 0], [7, 4, 1], [8, 5, 2], [8, 4, 0], [6, 4, 2]]
sq = [[0]*3]*3
totalsymbols = [0,0]
#Win function
def winner(win):
    if win == 1:
        return "O"
    elif win == 0:
        return "X" 
    else:
        return "Draw"

#Game loop
def main():
    winnersym = 0
    turn = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        mouse_pos = pg.mouse.get_pos()
        for i in range(9):
            win.blit(gridBlock, blockrect[i])
            if blockrect[i].collidepoint(mouse_pos):
                if pg.mouse.get_pressed()[0] and grid[i] == [0,0] and turn == 1:                
                    crossrect[i] = cross.get_rect(center = (blockcord[i]))
                    grid[i] = [crossrect[i] , 0, blockcord[i]]
                    turn = 0
                elif pg.mouse.get_pressed()[0] and grid[i] == [0,0] and turn == 0:
                    circlerect[i] = circle.get_rect(center = (blockcord[i]))
                    grid[i] = [circlerect[i], 1, blockcord[i]]
                    turn = 1

        

        #No overlapping of cross
        for i in range(9):
            if grid[i] != 0:
                if grid[i][1] == 0:
                    win.blit(cross, crossrect[i])
                elif grid[i][1] == 1:
                    win.blit(circle, circlerect[i])
        if [0,0] not in grid:
            for i in range(9):
                for j in range(9):
                    for k in range(9):
                        if (grid[i][1] == grid[j][1] == grid[k][1]) and ([i,j,k] in winpos):
                            winnersym = winner(grid[i][1])
                            break
            return(winnersym)
        
        pg.display.update() 
        Clock.tick(60)       
