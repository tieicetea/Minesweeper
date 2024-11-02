import pygame
from Tile import *
import math as m
import random as r

class Grid:

    def __init__(self, screen):
        self.screen = screen
        self.started = False
        self.minesSpawned = False
        self.lost = False
        self.won = False
        self.revealed = 0

    def setup(self, difficulty):
        self.lost = False
        self.minesSpawned = False
        self.started = True

        if difficulty == 'easy':
            self.numMines = 10
            self.flags = 10
            self.x = 10
            self.y = 8
        elif difficulty == 'medium':
            self.numMines = 40
            self.flags = 40
            self.x = 18
            self.y = 14
        elif difficulty == 'hard':
            self.numMines = 99
            self.x = 24
            self.flags = 99
            self.y = 20

        self.xStart = (600 - 20*self.x) / 2
        self.yStart = (600 - 20*self.y) / 2

        self.tileList = []

        for i in range(self.x * self.y):
            self.tileList.append(Tile(i, *self.numToCord(i)))
            #print(self.numToCord(i))

        self.startTime = pygame.time.get_ticks()

    


    def draw(self):
        allFont = pygame.font.Font("freesansbold.ttf", 30)

        if self.started and not self.lost and not self.won:
            for i in range(self.x * self.y):
                self.tileList[i].draw(self.screen)

            #time

            

            # timeText = allFont.render('Time: ', True, "White", "gray10")
            # timeRect = timeText.get_rect()
            # timeRect.center = (100, 10)
            # self.screen.blit(timeText, timeRect)

            mins = int((pygame.time.get_ticks() - self.startTime) / 60000)
            secs = (int (m.trunc((pygame.time.get_ticks() - self.startTime) / 1000)))
            decimals = (m.trunc((pygame.time.get_ticks() - self.startTime)/10) % 100)
        
            accTimeText = allFont.render("time: " + str(secs), True, "White", "gray10")  
                    
            
            accTimeRect = accTimeText.get_rect()
            accTimeRect.center = (200, 40)
            self.screen.blit(accTimeText, accTimeRect)


            flagText = allFont.render("flags: " + str(self.flags), True, "White", "gray10")
            flagRect = flagText.get_rect()
            flagRect.center = (400, 40)
            self.screen.blit(flagText, flagRect)

            #board, numbers, flags

        elif self.lost:

            bigFont = pygame.font.Font("freesansbold.ttf", 40)

            loseText = bigFont.render("You Lost!", True, "red", "gray10")
            loseRect = loseText.get_rect()
            loseRect.center = (300, 300)
            self.screen.blit(loseText, loseRect)

        elif self.won:

            bigFont = pygame.font.Font("freesansbold.ttf", 40)

            loseText = bigFont.render("You Won!", True, "green", "gray10")
            loseRect = loseText.get_rect()
            loseRect.center = (300, 300)
            self.screen.blit(loseText, loseRect)
    
        elif not self.started:
            #select difficulty screen

            selectText = allFont.render("Select your Difficulty", True, "White", "gray10")
            selectRect = selectText.get_rect()
            selectRect.center = (300, 50)
            
            pygame.draw.rect(self.screen, "green", pygame.Rect(150, 115, 300, 70))
            pygame.draw.rect(self.screen, "orange", pygame.Rect(150, 195, 300, 70))
            pygame.draw.rect(self.screen, "red", pygame.Rect(150, 275, 300, 70))

            
            diffFont = pygame.font.Font("freesansbold.ttf", 50)

            easyText = diffFont.render("EASY", False, "white")
            easyRect = easyText.get_rect()
            easyRect.center = (300, 150)

            medText = diffFont.render("MEDIUM", False, "white")
            medRect = medText.get_rect()
            medRect.center = (300, 230)

            hardText = diffFont.render("HARD", False, "white")
            hardRect = hardText.get_rect()
            hardRect.center = (300, 310)


            self.screen.blit(selectText, selectRect)
            self.screen.blit(easyText, easyRect)
            self.screen.blit(medText, medRect)
            self.screen.blit(hardText, hardRect)





            pass






    def numToCord(self, num):
        x = self.xStart + m.floor(num % self.x) * Tile.dim
        y = self.yStart + m.floor(num / self.x) * Tile.dim

        return (x, y)
    
    def cordToNum(self, x, y):
        xCord = m.floor((x - self.xStart) / Tile.dim)
        yCord = m.floor((y - self.yStart) / Tile.dim)

        return (yCord * self.x) + xCord

    
    def mines(self, mineList):
        self.minesSpawned = True

        for i in (mineList):
            self.tileList[i].mine = True
            self.tileList[i].adjacent = -1

        for i in range(self.x * self.y):
            if self.tileList[i].mine: 
                #print('mine ', i)
                continue

            xNum, yNum = self.numToCord(i)

            #print(xNum)

            xNum = (int(xNum) - self.xStart) / Tile.dim
            yNum = (int(yNum) - self.yStart) / Tile.dim
            
            
            #print(xNum, yNum)

            if (xNum != 0.0 and yNum != 0.0 and self.tileList[i-self.x - 1].mine): self.tileList[i].adjacent += 1 # top left

            if (yNum != 0.0 and self.tileList[i-self.x].mine): self.tileList[i].adjacent += 1 # top 

            if (yNum != 0.0 and xNum != self.x - 1.0 and self.tileList[i-self.x + 1].mine): self.tileList[i].adjacent += 1 # top right

            if (xNum != 0.0 and self.tileList[i - 1].mine): self.tileList[i].adjacent += 1 # left
  
            if (xNum != self.x - 1.0 and self.tileList[i + 1].mine): self.tileList[i].adjacent += 1 # right

            if (xNum != 0.0 and yNum != self.y - 1.0 and self.tileList[i+self.x - 1].mine): self.tileList[i].adjacent += 1 # bot left not working properly

            if (yNum != self.y - 1.0 and self.tileList[i + self.x].mine): self.tileList[i].adjacent += 1 # bot

            if (xNum != self.x - 1.0 and yNum != self.y - 1.0 and self.tileList[i + self.x + 1].mine): self.tileList[i].adjacent += 1 # bot right

    def reveal(self, cord):

        xNum, yNum = cord



        if (xNum >= self.xStart and xNum < self.xStart + self.x * Tile.dim) and (yNum >= self.yStart and yNum < self.yStart + self.y * Tile.dim):
            num = self.cordToNum(*cord)

            

        

            if (self.tileList[num].mine):
                self.lost = True
            elif not self.tileList[num].revealed:
                self.revealed += 1

            self.tileList[num].reveal()

            if self.tileList[num].adjacent == 0:

                visited = [False for i in range(self.x * self.y)]#bool listx
                visited[num] = True
                self.revealWaterfall(num, visited)

        if self.revealed == self.x * self.y - self.numMines:
            self.won = True

        #print(self.revealed)




    def revealWaterfall(self, num, visited):
        
        if (num < 0 or num >= self.x * self.y):
            return
        
        if not self.tileList[num].revealed:
            self.revealed += 1

        self.tileList[num].reveal()
       

        visited[num] = True

        if (self.tileList[num].adjacent == 0): # this isn't working, its wrapping the edges

            if (num - self.x - 1 >= 0 and num % self.x != 0 and not visited[num-self.x-1]): # and num % row != 0
                self.revealWaterfall(num-self.x-1, visited)

            if (num - self.x >= 0 and not visited[num-self.x]):
                self.revealWaterfall(num-self.x, visited)

            if (num - self.x + 1 >= 0 and num % self.x != self.x - 1 and not visited[num-self.x+1]): # and num % row != row - 1
                self.revealWaterfall(num-self.x+1, visited)

            if (num - 1 >= 0 and num % self.x != 0 and not visited[num-1]):
                self.revealWaterfall(num-1, visited)

            if (num + 1 < self.x * self.y and num % self.x != self.x - 1 and not visited[num+1]):
                self.revealWaterfall(num + 1, visited)

            if (num + self.x - 1 < self.x * self.y and num % self.x != 0 and not visited[num+self.x-1]):
                self.revealWaterfall(num + self.x - 1, visited)

            if (num + self.x < self.x * self.y and not visited[num+self.x]):
                self.revealWaterfall(num+self.x, visited)

            if (num + self.x + 1 < self.x * self.y and num % self.x != self.x - 1 and not visited[num+self.x+1]):
                self.revealWaterfall(num+self.x+1, visited)
            

    def flag(self, cord):
        xNum, yNum = cord



        if (xNum >= self.xStart and xNum < self.xStart + self.x * Tile.dim) and (yNum >= self.yStart and yNum < self.yStart + self.y * Tile.dim):
            num = self.cordToNum(*cord)
            self.tileList[num].flagged = not self.tileList[num].flagged
            if (self.tileList[num].flagged):
                self.flags -= 1
            else:
                self.flags += 1
            

            

        
    

    def genMineList(self, cord):

        xNum, yNum = cord

        mineList = set()

        if (xNum >= self.xStart and xNum < self.xStart + self.x * Tile.dim) and (yNum >= self.yStart and yNum < self.yStart + self.y * Tile.dim):
            num = self.cordToNum(*cord)
            
            while (len(mineList) < self.numMines):
                x = int(m.floor(r.random() * self.x * self.y))
                if not ((x >= num - 1 and x <= num + 1) or (x >= num - self.x - 1 and x <= num - self.x + 1) or (x >= num + self.x - 1 and x <= num + self.x + 1)):
                    mineList.add(x)


        self.mines(mineList)


        #print(mineList)




        pass


    def lose (self):
        pass



# pygame.init()
# pygame.font.init()

# screen = pygame.display.set_mode((600, 600))

# clock = pygame.time.Clock()
# running = True

# grid = Grid('hard')

# list = [5, 9, 10, 12, 16, 18]

# grid.mines(list)

# pygame.key.set_repeat(50)
# #block1 = Block("red", player_pos.x, player_pos.y)

# #run all possible moves, evaluate how good the move is

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
                
                
#                 keys = pygame.key.get_pressed()

#         if event.type == pygame.MOUSEBUTTONUP:
#             if (event.button == 1):
#                 grid.reveal(pygame.mouse.get_pos())


#                 # 1 - left click
#                 # 2 - middle click
#                 # 3 - right click
#                 # 4 - scroll up
#                 # 5 - scroll down


                        
                
                
        
    
    


#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("gray10")
    
#     #block1.update_pos(player_pos.x, player_pos.y)
#     #block1.draw(screen)
#     #usingPiece.update_pos(player_pos.x, player_pos.y)
#     #usingPiece.draw(screen)
    

#     grid.draw(screen)

    
    

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     # limits FPS to 60
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     #dt = clock.tick(60) / 1000
#     clock.tick(120)
# pygame.quit()
