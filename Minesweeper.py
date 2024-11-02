from Grid import *
from Tile import *

def main ():
    
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((600, 600))

    clock = pygame.time.Clock()
    running = True

    grid = Grid(screen)
    

    # list = [5, 9, 10, 12, 16, 18]

    # grid.mines(list)

    pygame.key.set_repeat(50)
    #block1 = Block("red", player_pos.x, player_pos.y)

    #run all possible moves, evaluate how good the move is

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                
                    
                keys = pygame.key.get_pressed()

            if event.type == pygame.MOUSEBUTTONUP:

                
                if (event.button == 1):
                    
                    if (not grid.started):
                        x, y = pygame.mouse.get_pos()
                        
                        if (x >= 150 and x <= 450 and y >= 115 and y <= 185):
                            grid.setup("easy")
                        elif (x >= 150 and x <= 450 and y >= 195 and y <= 265):
                            grid.setup("medium")
                        elif (x >= 150 and x <= 450 and y >= 275 and y <= 345):
                            grid.setup("hard")
                        
                    elif (not grid.minesSpawned):
                        grid.genMineList(pygame.mouse.get_pos())
                        grid.reveal(pygame.mouse.get_pos())
                    else:
                        grid.reveal(pygame.mouse.get_pos())
                if (event.button == 3):
                    grid.flag(pygame.mouse.get_pos())
                        


                    # 1 - left click
                    # 2 - middle click
                    # 3 - right click
                    # 4 - scroll up
                    # 5 - scroll down


                            
                    
                    
            
        
        


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray10")
        
        #block1.update_pos(player_pos.x, player_pos.y)
        #block1.draw(screen)
        #usingPiece.update_pos(player_pos.x, player_pos.y)
        #usingPiece.draw(screen)
        

        grid.draw()

        
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        #dt = clock.tick(60) / 1000
        clock.tick(120)
    pygame.quit()
    
    
    
    pass



main()