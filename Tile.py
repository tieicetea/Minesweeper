import pygame
import pygame.color

class Tile:
    dim = 20
    def __init__(self, num, x, y):
        self.num = num
        # self.color = pygame.Color('0x63c8f6') if self.num % 2 == 0 else pygame.Color('0x174bcd')
        self.x = x
        self.y = y
        self.color = pygame.Color('0x14342B') if (x/self.dim + y/self.dim) % 2 == 0 else pygame.Color('0x709775')
        
        self.flagged = False
        self.mine = False
        self.revealed = False
        self.adjacent = 0

    def draw (self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.dim, self.dim), 0)
        
        if self.revealed and self.adjacent > 0:
            allFont = pygame.font.Font("freesansbold.ttf", 15)
            text = allFont.render(str(self.adjacent), True, "Black")
            textRect = text.get_rect()
            textRect.center = (self.x + 10, self.y + 10)
            screen.blit(text, textRect)

        if self.flagged:
            pygame.draw.circle(screen, '0xEE4B2B', (self.x + self.dim/2, self.y + self.dim/2), self.dim/4)

        
        

    def reveal(self):
        self.revealed = True
        
        if (self.mine):
            self.color = pygame.Color('0xEE4B2B')
        else:
            self.color = pygame.Color('0x8e9dcc') if (self.x/self.dim + self.y/self.dim) % 2 == 0 else pygame.Color('0xd9dbf1')

        
    #colors, cyan (#63c8f6 or #92edff), and deeper blue (#174bcd), similar to my bkg
    #outline is white (#fef8fe) and the under is pink (#fd76dd) and purple (9d82ea), all similar to my bkg
    






