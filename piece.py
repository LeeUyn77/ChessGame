import pygame
DEAD = 0
SELECT = 1
ALIVE = 2
class piece:
    def __init__(self,Type):
        self.status = ALIVE
        self.type = Type
        if Type == "bp" :
            self.Image = pygame.transform.scale(pygame.image.load("black_pawn.png"), (80, 80))
        elif Type == "wp" :
            self.Image = pygame.transform.scale(pygame.image.load("white_pawn.png"), (80, 80))
    def get_image(self):
        return self.Image
    
    
    