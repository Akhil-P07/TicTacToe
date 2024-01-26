from TicTacToe import main
from Mainmenu import menuMain
from playagain import playagain
from Mainmenu import menuMain
from TicTacToe import main
end = 1
while end == 1:
    menuMain()
    a = main()
    x = playagain(a)
    if x != 1:
        quit()