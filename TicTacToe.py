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
<<<<<<< HEAD
        print("O")
    elif win == 0:
        print("X")
    else:
        print("Draw")
#Grid class
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
                if pg.key.get_pressed()[pg.K_x] and grid[i] == [0,0]:                
                    crossrect[i] = cross.get_rect(center = (blockcord[i]))
                    grid[i] = [crossrect[i] , 0, blockcord[i], True]
                elif pg.key.get_pressed()[pg.K_o] and grid[i] == [0,0]:
                    circlerect[i] = circle.get_rect(center = (blockcord[i]))
                    grid[i] = [circlerect[i], 1, blockcord[i]]
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
                            return winner(grid[i][1])
                            
            return winner(-1)

        pg.display.update() 
        Clock.tick(60)        
=======
        print("O wins")
    elif win == 0:
        print("X wins")
    else:
        print("Draw")
#Game loop

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    mouse_pos = pg.mouse.get_pos()
    for i in range(9):
        win.blit(gridBlock, blockrect[i])
        if blockrect[i].collidepoint(mouse_pos):
            if pg.key.get_pressed()[pg.K_x] and grid[i] == [0,0]:                
                crossrect[i] = cross.get_rect(center = (blockcord[i]))
                grid[i] = [crossrect[i] , 0, blockcord[i]]
            elif pg.key.get_pressed()[pg.K_o] and grid[i] == [0,0]:
                circlerect[i] = circle.get_rect(center = (blockcord[i]))
                grid[i] = [circlerect[i], 1, blockcord[i]]
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
                        winner(grid[i][1])
                        print(i,j,k)
                        quit()
        winner(-1)
        quit()

    pg.display.update() 
    Clock.tick(60)        

>>>>>>> df3922aa790f6004e25011d96bd394b94281ecee
